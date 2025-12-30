[![DOI](https://zenodo.org/badge/1124444957.svg)](https://doi.org/10.5281/zenodo.18080288)
# KRR (Korean Reversible Romanization) 🇰🇷

> **"No Ambiguity. 100% Reversible. AI-Ready."**

## What is this?
KRR is a strictly logical romanization system for Hangul.
It creates a **bijective (1-to-1) mapping** between Hangul characters and ASCII strings.

- **For Humans:** It preserves the morphological meaning (e.g., `goog\bab`).
- **For Machines:** It allows O(1) complexity search and perfect data restoration.

## Why use this?
1. **Zero Ambiguity:** Solves the `Gang` (River vs Angle) problem.
2. **AI Friendly:** Reduces token count and handles 'Niga' (You are) safely without triggering hate-speech filters.
3. **Open Source:** Apache 2.0 License. Free for enterprise use.

## How to use
```python
from krr_v2 import KRR

print(KRR.encode("한글")) 
# Output: han\ge~l

print(KRR.decode("han\ge~l"))
# Output: 한글
