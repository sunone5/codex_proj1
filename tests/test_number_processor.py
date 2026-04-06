"""Tests for NumberProcessor using pytest."""

import pytest

from src.number_processor import NumberProcessor


@pytest.mark.parametrize(
    ("first", "second", "expected"),
    [
        (20, 30, 600),
        (40, 30, 70),
        (50, 20, 1000),
        (1, 1001, 1002),
        (-10, 200, -2000),
    ],
)
def test_calculate_applies_threshold_rule(first: int, second: int, expected: int) -> None:
    processor = NumberProcessor()

    result = processor.calculate(first, second)

    assert result == expected


def test_calculate_with_custom_threshold() -> None:
    processor = NumberProcessor(threshold=10)

    assert processor.calculate(3, 4) == 7
