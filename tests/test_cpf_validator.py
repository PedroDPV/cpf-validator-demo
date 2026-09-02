"""Unit tests for the CPF validator."""

import pytest

from src.cpf_validator import clean_cpf, format_cpf, is_valid_cpf, validate_cpf
from src.exceptions import InvalidCPFFormatError
from src.synthetic_data import generate_synthetic_cpf


def test_clean_cpf_removes_formatting_characters() -> None:
    assert clean_cpf("123.456.789-09") == "12345678909"


def test_clean_cpf_rejects_invalid_characters() -> None:
    with pytest.raises(InvalidCPFFormatError):
        clean_cpf("123.abc.789-09")


def test_format_cpf_adds_standard_punctuation() -> None:
    assert format_cpf("12345678909") == "123.456.789-09"


def test_synthetic_cpf_is_valid() -> None:
    cpf = generate_synthetic_cpf(seed=1)
    assert is_valid_cpf(cpf) is True


def test_synthetic_cpf_generation_is_deterministic_with_seed() -> None:
    first = generate_synthetic_cpf(seed=7)
    second = generate_synthetic_cpf(seed=7)
    assert first == second


@pytest.mark.parametrize(
    "known_invalid",
    [
        "111.111.111-11",
        "000.000.000-00",
        "123.456.789-00",
    ],
)
def test_known_invalid_cpfs_are_rejected(known_invalid: str) -> None:
    assert is_valid_cpf(known_invalid) is False


def test_validate_cpf_reports_error_details_for_invalid_input() -> None:
    result = validate_cpf("123")
    assert result.is_valid is False
    assert result.error is not None


def test_formatted_and_unformatted_synthetic_cpf_are_equivalent() -> None:
    formatted = generate_synthetic_cpf(seed=99, formatted=True)
    unformatted = generate_synthetic_cpf(seed=99, formatted=False)
    assert clean_cpf(formatted) == unformatted


def test_valid_cpf_result_includes_formatted_output() -> None:
    cpf = generate_synthetic_cpf(seed=5)
    result = validate_cpf(cpf)
    assert result.is_valid is True
    assert result.formatted == cpf
