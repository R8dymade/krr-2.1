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
```

## How to install

For now, the package is not yet available on pypi, but it can either be installed directly from github:

```bash
# Using https
pip install git+https://github.com/R8dymade/krr-2.1.git
# using ssh
pip install git+ssh://git@github.com:R8dymade/krr-2.1.git
```

I can then be used just as above.

Alternatively, for developers, with the repository cloned, install the path to the directory, normally or in editable mode will also make the package useable.

```
git clone <path to repository ssh/http>
cd krr-2.1

# normal install
pip install .

# or editable install to track changes
pip install -e .
```

## Running tests

The tests can be run with pytest installed by calling

```
pytest
```
