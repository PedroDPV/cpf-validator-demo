# Security Policy

This repository is a small, self-contained portfolio demo. It does not collect, store, or transmit any personal data.

## Data handling

- The validator only checks the mathematical structure of a CPF-like string; it does not look up, store, or verify the number against any real registry or database.
- The synthetic CPF generator (`src/synthetic_data.py`) produces numbers with valid check digits for demonstration and testing only. These numbers are generated locally with Python's `random` module and are not derived from, and are not associated with, any real person.
- No CPF numbers, generated or otherwise, are logged, persisted to disk, or sent over the network by this project.

## Secure coding practices applied

- No hardcoded secrets, credentials, or network calls anywhere in this codebase.
- Input is validated defensively before any processing (format check, length check, known-invalid pattern check), and invalid input raises specific, typed exceptions instead of failing silently.
- The regular expression used for input sanitization is anchored and restrictive to avoid unexpected matches.
- Dependencies are pinned in `requirements.txt` and limited to a testing framework; the core library has zero runtime dependencies.

## Reporting a concern

This is a personal portfolio project and not a production service. If you notice an issue with the validation logic itself, please open a GitHub issue on this repository.
