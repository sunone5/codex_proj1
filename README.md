# Number Processor (OOP + TDD)

This project contains a small Python OOP program with type hints.

## Problem rule
Given two integer numbers:
- Return their **product** if the product is less than or equal to `1000`.
- Otherwise, return their **sum**.

## Implementation
- `NumberProcessor` class is implemented in `src/number_processor.py`.
- Main method: `calculate(first: int, second: int) -> int`
- Includes configurable `threshold` (default `1000`).

## Tests (pytest)
Run:

```bash
python -m pytest
```

## Coverage report
This environment may not include `pytest-cov`, so coverage can be generated using Python's built-in `trace` module:

```bash
python -m trace --count --summary -m pytest -q
```
