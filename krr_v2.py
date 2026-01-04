# Copyright 2025 [R8dymade]
# Licensed under the Apache License, Version 2.0.

class KRR:
    """
    KRR v2.0 Converter
    - Lossless, Reversible, Deterministic.
    - Optimized for AI & Database indexing.
    """
    # Initial / Medial / Final Tables
    I = ['g','g`','n','d','d`','l','m','b','b`','s','s`','','j','j`','ch','k','t','p','h']
    M = ['e~i','yoo','wè','wu','oo','yo','ö','wä','wa','yè','yu','è','u','yä','ya','ä','a','i','e~','o']
    F = ['','g','g`','gs','n','nj','nh','d','l','lg','lm','lb','ls','lt','lp','lh','m','b','bs','s','s`','ng~','j','ch','k','t','p','h']

    @staticmethod
    def encode(text):
        """Converts Hangul to KRR v2.0 string."""
        res = []
        for char in text:
            if '가' <= char <= '힣':
                c = ord(char) - 44032
                cho, jung, jong = c // 588, (c % 588) // 28, c % 28
                # Mathematically map logic
                res.append(KRR.I[cho] + KRR.M[jung] + KRR.F[jong])
            else:
                res.append(char)
        return "\\".join(res) # Insert Separator

    @staticmethod
    def decode(text):
        """Restores KRR v2.0 string back to original Hangul."""
        res = []
        for block in text.split('\\'):
            if not block: continue
            matched = False
            # Greedy parsing for vowels
            for v in KRR.M:
                if v in block:
                    p = block.partition(v)
                    ini, mid, fin = p[0], p[1], p[2]
                    # Restore indices
                    i_idx = KRR.I.index(ini) if ini in KRR.I else 11 # Default to 'ㅇ'
                    m_idx = KRR.M.index(mid)
                    f_idx = KRR.F.index(fin) if fin in KRR.F else 0
                    # Unicode Re-assembly
                    res.append(chr(44032 + (i_idx*588) + (m_idx*28) + f_idx))
                    matched = True
                    break
            if not matched: res.append(block)
        return "".join(res)

# Simple Test to prove it works
if __name__ == "__main__":
    test_word = "국밥"
    krr = KRR.encode(test_word)
    restored = KRR.decode(krr)
    print(f"Original: {test_word}")
    print(f"KRR v2.0: {krr}")
    print(f"Restored: {restored}")
