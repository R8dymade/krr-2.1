# KRR v2.0: A Deterministic and Lossless Romanization System for Korean Language Processing

**Author:** [R8dymade]
**Date:** December 2025
**License:** Apache License 2.0

---

## 1. Introduction & Philosophy
**KRR v2.0** (Korean Romanization for Robots) is a next-generation romanization system designed specifically for **AI, Database Indexing, and Computational Linguistics**.

Unlike the current national standard (Revised Romanization, RR), which prioritizes phonetic approximation for human speech, KRR v2.0 focuses on **Data Integrity, Reversibility, and Morphological Preservation**.

> **Homage to King Sejong**
> This system is structurally inspired by the modular architecture of **Hunminjeongeum** (1446). We did not invent this structure; we simply built a **digital bridge** to carry King Sejong's logical design into the modern ASCII-based computing environment.

## 2. The Problem
Current standards treat Hangul as "sound," causing fatal issues in tech:
1.  **Irreversibility:** `신라` → `Silla`. Decoding `Silla` results in `실라`. (Original data lost).
2.  **Ambiguity:** `Gang` could be `강` or `각+ㅇ`.
3.  **Safety (The 'Niga' Issue):** The pronoun `니가` (You are) is transliterated as `Niga`, triggering hate speech filters globally.

## 3. The Solution: KRR v2.0
We utilize a **Deterministic 1:1 Mapping** algorithm using standard ASCII and 3 control keys.

### 3.1. The 3 Control Keys
| Key | Function | Example |
| :---: | :--- | :--- |
| **` ` ` (Backtick)** | **Mutator** (Tension/Vowel Shift) | `g` (ㄱ) + `` ` `` → `g` ` (ㄲ) <br> `o` (ㅗ) + `` ` `` → `ö` (ㅚ) |
| **`~` (Tilde)** | **Identifier** (Unique Marker) | `e` (ㅔ) + `~` → `e~` (ㅡ) <br> `ng` (ㄴ+ㄱ) + `~` → `ng~` (ㅇ 받침) |
| **`\` (Backslash)** | **Separator** (Morpheme Boundary) | `goog\bab` (Preserves `goog` and `bab`) |

### 3.2. Safety by Design
KRR structurally separates particles.
- **Hangul:** `니가` (You + Subject Marker)
- **KRR:** `ni` + `ga`
- **Effect:** AI and filters can clearly distinguish grammatical patterns from racial slurs.

## 4. Conclusion
KRR v2.0 reduces the 11,172 Hangul syllables into a predictable, mathematically convertible ASCII set. It is the most efficient protocol for **AI Tokenization** and **Global Search Engines**.

## 5. Copyright & LicenseNotice

**Copyright © 2025 [R8dymade]**

This project is licensed under the **Apache License, Version 2.0** (the "License").
You may not use this file except in compliance with the License.

> **Disclaimer of Warranty:**
> Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an **"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND**, either express or implied. See the License for the specific language governing permissions and limitations under the License.

For the full license text, please refer to the `LICENSE` file in the repository.
