#!/usr/bin/env python3
# Copyright 2025 [R8dymade]
# Licensed under the Apache License, Version 2.0.

"""
KRR (Korean Romanization Rules) v2.1.1
Lossless, Reversible, Deterministic Romanization Library.

This module provides functions to convert Hangul to KRR romanized string
and decode it back to the original Hangul. It guarantees a 1:1 mapping
suitable for AI tokenization and database indexing.
"""

import sys
import argparse

__version__ = '2.1.1'

# ==========================================
# Configuration & Constants
# ==========================================

SEPARATOR = "\\"

# Unicode 11.0 Hangul Jamo Standards
# 19 Initial Consonants (Onset)
INITIALS = [
    'g', 'g`', 'n', 'd', 'd`', 'l', 'm', 'b', 'b`', 's',
    's`', '', 'j', 'j`', 'ch', 'k', 't', 'p', 'h'
]

# 21 Medial Vowels (Nucleus)
MEDIALS = [
    'a', 'ä', 'ya', 'yä', 'u', 'è', 'yu', 'yè', 'o', 'wa',
    'wä', 'ö', 'yo', 'oo', 'ü', 'wè', 'wi', 'yoo', 'e~', 'e~i', 'i'
]

# 28 Final Consonants (Coda)
FINALS = [
    '', 'g', 'g`', 'gs', 'n', 'nj', 'nh', 'd', 'l', 'lg', 'lm',
    'lb', 'ls', 'lt', 'lp', 'lh', 'm', 'b', 'bs', 's', 's`',
    'ng~', 'j', 'ch', 'k', 't', 'p', 'h'
]

# ==========================================
# Optimization (Pre-computed lookups)
# ==========================================

# O(1) Lookup tables for decoding
INITIAL_MAP = {val: idx for idx, val in enumerate(INITIALS)}
MEDIAL_MAP = {val: idx for idx, val in enumerate(MEDIALS)}
FINAL_MAP = {val: idx for idx, val in enumerate(FINALS)}

# Sorted by length (descending) to ensure greedy matching in tokenizer
_SORTED_MEDIALS = sorted(MEDIALS, key=len, reverse=True)


# ==========================================
# Core Functions
# ==========================================

def encode(text: str) -> str:
    """
    Encodes Hangul text into KRR string.
    
    Automatically inserts separators between Hangul syllables to resolve 
    VCCV/VCV boundary ambiguity (e.g., distinguishing 'gak-ka' vs 'ga-kka').
    
    Args:
        text (str): Input Hangul text.
        
    Returns:
        str: Romanized text with separators.
    """
    result = []
    for char in text:
        if '가' <= char <= '힣':
            # Calculate Unicode Offset
            code = ord(char) - 44032
            
            # Decompose into Onset, Nucleus, Coda
            onset = code // 588
            nucleus = (code % 588) // 28
            coda = code % 28
            
            syllable = INITIALS[onset] + MEDIALS[nucleus] + FINALS[coda]
            result.append(syllable)
        else:
            result.append(char)
    
    # Insert SEPARATOR between all blocks to prevent boundary ambiguity
    return SEPARATOR.join(result)


def decode(text: str) -> str:
    """
    Decodes KRR string back to original Hangul.
    
    Handles both standard SEPARATOR and spaces as delimiters for robust parsing.
    
    Args:
        text (str): KRR romanized string.
        
    Returns:
        str: Reconstructed Hangul text.
    """
    result = []
    # Clean input from potential shell quoting
    text = text.strip('"\'')
    
    # Treat spaces as block delimiters alongside SEPARATOR
    # This logic allows 'sang~ yu' to be parsed as 'sang~' and 'yu'
    text = text.replace(" ", f"{SEPARATOR} {SEPARATOR}")
    
    blocks = text.split(SEPARATOR)
    
    for block in blocks:
        if not block:
            continue
            
        matched = False
        # Greedy parsing for nucleus to handle composite vowels correctly
        for vowel in _SORTED_MEDIALS:
            if vowel in block:
                p = block.partition(vowel)
                onset_str, nucleus_str, coda_str = p[0], p[1], p[2]
                
                # Validate component existence in lookup tables
                if onset_str in INITIAL_MAP and coda_str in FINAL_MAP:
                    onset = INITIAL_MAP[onset_str]
                    nucleus = MEDIAL_MAP[nucleus_str]
                    coda = FINAL_MAP[coda_str]
                    
                    # Reconstruct Hangul character from Unicode components
                    char_code = 44032 + (onset * 588) + (nucleus * 28) + coda
                    result.append(chr(char_code))
                    matched = True
                    break
                    
        if not matched:
            result.append(block)
            
    return "".join(result)


# ==========================================
# CLI Entry Point
# ==========================================

def main():
    parser = argparse.ArgumentParser(description="KRR v2.1.1 - Korean Romanization Rules")
    parser.add_argument("text", help="Input text to process")
    parser.add_argument("-d", "--decode", action="store_true", help="Decode mode")
    
    args = parser.parse_args()
    
    if args.decode:
        print(decode(args.text))
    else:
        # Wrap output in quotes to handle special characters in shell
        print(f'"{encode(args.text)}"')

if __name__ == "__main__":
    main()
