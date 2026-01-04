[![DOI](https://zenodo.org/badge/1124444957.svg)](https://doi.org/10.5281/zenodo.18080288)
# KRR (Korean Reversible Romanization) 🇰🇷

> **"No Ambiguity. 100% Reversible. AI-Ready."**

## What is this?
KRR is a strictly logical romanization system for Hangul.
It creates a **bijective (1-to-1) mapping** between Hangul characters and ASCII strings.

- **For Humans:** It preserves the morphological meaning (e.g., `goog\bab`).
- **For Machines:** It allows O(1) complexity search and perfect data restoration.

## Why use this?
1. **Zero Ambiguity:** Solves the `Gang` (River vs Liver+g) problem.
3. **AI Friendly:** Reduces token count and handles 'Niga' (You are) safely without triggering hate-speech filters.
4. **Open Source:** Apache 2.0 License. Free for enterprise use.

## How to use
```pycon
>>> import krr

>>> krr.encode("한글")
'han\\ge~l'

>>> krr.decode("han\ge~l")
'한글'

```

## How to install

For now, the package is not yet available on pypi, but it can either be installed directly from github:

```bash
# Using https
pip install git+https://github.com/R8dymade/krr.git
# using ssh
pip install git+ssh://git@github.com:R8dymade/krr.git
```

I can then be used just as above.

Alternatively, for developers, with the repository cloned, install the path to the directory, normally or in editable mode will also make the package useable.

```
git clone <path to repository ssh/http>
cd krr

# normal install
pip install .

# or editable install to track changes
pip install -e .
```

## Running tests

The tests can be run with pytest (and pytest-doctestplus for README documentation) installed by calling

```
# Unit tests
pytest

# Doctests to include README
pytest --doctest-plus --doctest-glob '*.md'
```
