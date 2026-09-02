"""Core validation logic for Brazilian CPF (Cadastro de Pessoas Fisicas) numbers.

This module implements the official CPF check-digit algorithm from scratch,
with no external dependencies. It follows clean code principles: small pure
functions, explicit typing, and a clear separation between parsing,
structural validation, and check-digit verification.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Optional

from src.exceptions import (
    CPFCheckDigitError,
    CPFValidationError,
    InvalidCPFFormatError,
    InvalidCPFLengthError,
    KnownInvalidCPFError,
)

_ALLOWED_CHARACTERS_PATTERN = re.compile(r"^[\d.\-\s]+$")
_CPF_LENGTH = 11


@dataclass(frozen=True)
class CPFValidationResult:
    """Immutable result of a CPF validation attempt."""

    raw_input: str
    digits: str
    is_valid: bool
    formatted: Optional[str] = None
    error: Optional[str] = None


def clean_cpf(value: str) -> str:
    """Strip formatting characters (dots, dashes, whitespace) from a CPF string.

    Raises:
        InvalidCPFFormatError: if the value contains characters other than
            digits, dots, dashes or whitespace.
    """
    if not _ALLOWED_CHARACTERS_PATTERN.match(value):
        raise InvalidCPFFormatError(value)
    return re.sub(r"[.\-\s]", "", value)


def calculate_check_digit(digits: str, weight_start: int) -> int:
    """Calculate a single CPF check digit using the official weighted-sum algorithm."""
    total = sum(
        int(digit) * weight
        for digit, weight in zip(digits, range(weight_start, 1, -1))
    )
    remainder = (total * 10) % 11
    return 0 if remainder == 10 else remainder


def format_cpf(digits: str) -> str:
    """Format an 11-digit CPF string as XXX.XXX.XXX-XX."""
    return f"{digits[0:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:11]}"


def _ensure_length(digits: str) -> None:
    if len(digits) != _CPF_LENGTH:
        raise InvalidCPFLengthError(len(digits))


def _ensure_not_known_invalid(digits: str) -> None:
    if digits == digits[0] * _CPF_LENGTH:
        raise KnownInvalidCPFError(digits)


def _ensure_check_digits_match(digits: str) -> None:
    first_check_digit = calculate_check_digit(digits[:9], weight_start=10)
    second_check_digit = calculate_check_digit(
        digits[:9] + str(first_check_digit), weight_start=11
    )
    expected = f"{first_check_digit}{second_check_digit}"
    actual = digits[9:11]
    if expected != actual:
        raise CPFCheckDigitError(digits)


def validate_cpf(value: str) -> CPFValidationResult:
    """Validate a CPF, returning a structured result instead of raising.

    This is the primary entry point for consumers that prefer a result
    object over exception handling.
    """
    try:
        digits = clean_cpf(value)
        _ensure_length(digits)
        _ensure_not_known_invalid(digits)
        _ensure_check_digits_match(digits)
    except CPFValidationError as exc:
        return CPFValidationResult(
            raw_input=value,
            digits="",
            is_valid=False,
            error=str(exc),
        )
    return CPFValidationResult(
        raw_input=value,
        digits=digits,
        is_valid=True,
        formatted=format_cpf(digits),
    )


def is_valid_cpf(value: str) -> bool:
    """Convenience boolean check, useful for simple call sites."""
    return validate_cpf(value).is_valid
