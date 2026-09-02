"""Command-line demo for the CPF validator.

Run with: python -m src.cli
"""

from __future__ import annotations

from src.cpf_validator import validate_cpf
from src.synthetic_data import generate_synthetic_cpf


def _print_result(label: str, cpf: str) -> None:
    result = validate_cpf(cpf)
    status = "VALID" if result.is_valid else "INVALID"
    detail = result.formatted if result.is_valid else result.error
    print(f"[{status}] {label}: {cpf} -> {detail}")


def main() -> None:
    print("CPF Validator Demo (synthetic data only)\n")

    synthetic_valid = generate_synthetic_cpf(seed=42)
    _print_result("Synthetic valid CPF", synthetic_valid)

    known_invalid_examples = [
        "111.111.111-11",
        "123.456.789-00",
        "000.000.000-00",
        "abc.def.ghi-jk",
        "12345",
    ]
    for example in known_invalid_examples:
        _print_result("Known invalid example", example)


if __name__ == "__main__":
    main()
