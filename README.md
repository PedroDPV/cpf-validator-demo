# CPF Validator (Portfolio Demo)

This is a portfolio and demo project that implements a validator for Brazilian CPF (Cadastro de Pessoas Fisicas, the Brazilian individual taxpayer ID) numbers, built from scratch in Python with no external validation libraries.

**Disclaimer:** this repository never uses real CPF numbers. All examples and tests rely on synthetically generated numbers (see `src/synthetic_data.py`) that only satisfy the mathematical check-digit rule; they are not tied to, and must never be treated as, any real person's identity document. This is a simplified sample meant to illustrate clean code and validation design, not a production compliance tool.

## What it validates

- **Format:** the input may contain digits plus optional dots and a dash (e.g. `123.456.789-09`); anything else is rejected.
- **Length:** after removing formatting characters, the value must have exactly 11 digits.
- **Known invalid sequences:** CPFs where all 11 digits repeat (e.g. `111.111.111-11`) are rejected, even though some pass the check-digit math.
- **Check digits:** the two verification digits are recalculated using the official weighted-sum algorithm and compared against the input.

## Project structure

- `src/cpf_validator.py`: core validation and formatting logic, exposed as small pure functions.
- `src/exceptions.py`: specific exception types for each validation failure mode.
- `src/synthetic_data.py`: generates random, check-digit-valid CPFs for demos and tests only.
- `src/cli.py`: runnable command-line demo.
- `tests/test_cpf_validator.py`: unit tests covering valid, invalid, and edge-case inputs.
- `SECURITY.md`: data handling and secure coding practices applied in this demo.

## Design and engineering practices

- Single-responsibility functions: parsing, structural checks, and check-digit math are separated so each can be tested independently.
- A `CPFValidationResult` dataclass gives callers a structured, immutable result instead of forcing them to rely solely on exceptions.
- A typed exception hierarchy (`CPFValidationError` and subclasses) makes failure modes explicit and easy to handle selectively.
- Full type hints and docstrings throughout, with no hidden global state.

## Running locally

1. Create a virtual environment and install dependencies from `requirements.txt`.
2. Run the demo with `python -m src.cli`.
3. Run the tests with `pytest`.

## Tech stack

Python standard library only for the validator itself; `pytest` for the test suite.

## About this repository

This project is part of my professional portfolio and demonstrates clean code, defensive input validation, and software engineering practices applied to a small, self-contained problem. It is a sample built specifically for this purpose, not an export of employer code.
