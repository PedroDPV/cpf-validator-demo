"""Synthetic CPF generator used only for demos and tests.

Generates random, check-digit-valid CPF numbers for demonstration purposes.
These numbers are produced locally from random digits and are not tied to,
and must never be treated as, any real person's identity document.
"""

from __future__ import annotations

import random
from typing import Optional

from src.cpf_validator import calculate_check_digit, format_cpf


def generate_synthetic_cpf(formatted: bool = True, seed: Optional[int] = None) -> str:
    """Generate a random, check-digit-valid CPF for demo and test purposes only.

    Args:
        formatted: if True, returns the CPF as XXX.XXX.XXX-XX, otherwise as
            11 raw digits.
        seed: optional seed for reproducible output in tests.
    """
    rng = random.Random(seed)
    base_digits = "".join(str(rng.randint(0, 9)) for _ in range(9))

    first_check_digit = calculate_check_digit(base_digits, weight_start=10)
    second_check_digit = calculate_check_digit(
        base_digits + str(first_check_digit), weight_start=11
    )

    digits = f"{base_digits}{first_check_digit}{second_check_digit}"
    return format_cpf(digits) if formatted else digits
