"""Custom exceptions for the CPF validator package."""


class CPFValidationError(Exception):
    """Base exception for all CPF validation errors."""


class InvalidCPFFormatError(CPFValidationError):
    """Raised when the input contains characters other than digits, dots, dashes or spaces."""

    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(f"CPF '{value}' contains invalid characters.")


class InvalidCPFLengthError(CPFValidationError):
    """Raised when the cleaned CPF does not have exactly 11 digits."""

    def __init__(self, length: int) -> None:
        self.length = length
        super().__init__(f"CPF must have exactly 11 digits, got {length} digit(s).")


class KnownInvalidCPFError(CPFValidationError):
    """Raised when the CPF matches a known-invalid pattern, such as all repeated digits."""

    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(f"CPF '{value}' is a known invalid sequence.")


class CPFCheckDigitError(CPFValidationError):
    """Raised when the two CPF check digits do not match the computed values."""

    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(f"CPF '{value}' has invalid check digits.")
