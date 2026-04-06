"""Module containing OOP solution for processing two integers."""

from dataclasses import dataclass


@dataclass(frozen=True)
class NumberProcessor:
    """Process two integers based on product threshold rules."""

    threshold: int = 1000

    def calculate(self, first: int, second: int) -> int:
        """Return product if it is <= threshold; otherwise return sum."""
        product: int = first * second
        return product if product <= self.threshold else first + second
