# Calculator Module

A basic calculator module providing four fundamental arithmetic operations for Python developers. Built with type safety, clear error messages, and predictable behavior.

## Features

- **Four Operations**: Addition, subtraction, multiplication, and division
- **Type Safety**: Python 3.12+ type hints with runtime validation
- **Clear Errors**: Explicit error messages for invalid inputs and edge cases
- **IEEE 754 Compliant**: Standard floating-point arithmetic behavior
- **Zero Dependencies**: Pure Python implementation

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/calc.git
cd calc
```

## Usage

```python
from calculator import add, subtract, multiply, divide

# Addition
result = add(5, 3)  # 8
result = add(2.5, 3.7)  # 6.2

# Subtraction
result = subtract(10, 4)  # 6
result = subtract(5, 3)  # 2

# Multiplication
result = multiply(6, 7)  # 42
result = multiply(2.5, 4.0)  # 10.0

# Division (always returns float)
result = divide(10, 2)  # 5.0
result = divide(10, 3)  # 3.3333333333333335

# Error handling
try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(e)  # "Cannot divide by zero"

try:
    result = add("10", 5)
except TypeError as e:
    print(e)  # "Both arguments must be numbers (int or float)"
```

## API Reference

### `add(a: int | float, b: int | float) -> int | float`

Add two numbers together.

**Parameters:**
- `a`: First number (int or float)
- `b`: Second number (int or float)

**Returns:** Sum of a and b

**Raises:**
- `TypeError`: If either argument is not a number

**Examples:**
```python
add(5, 3)      # 8
add(2.5, 3.7)  # 6.2
add(0.1, 0.2)  # 0.30000000000000004 (IEEE 754 precision)
```

---

### `subtract(a: int | float, b: int | float) -> int | float`

Subtract b from a (returns a - b).

**Parameters:**
- `a`: Number to subtract from (int or float)
- `b`: Number to subtract (int or float)

**Returns:** Result of a - b

**Raises:**
- `TypeError`: If either argument is not a number

**Examples:**
```python
subtract(10, 4)   # 6
subtract(5, 3)    # 2
subtract(3, 10)   # -7
subtract(5, -3)   # 8
```

---

### `multiply(a: int | float, b: int | float) -> int | float`

Multiply two numbers.

**Parameters:**
- `a`: First number (int or float)
- `b`: Second number (int or float)

**Returns:** Product of a and b

**Raises:**
- `TypeError`: If either argument is not a number

**Examples:**
```python
multiply(6, 7)      # 42
multiply(2.5, 4.0)  # 10.0
multiply(5, -3)     # -15
```

---

### `divide(a: int | float, b: int | float) -> float`

Divide a by b (always returns float).

**Parameters:**
- `a`: Dividend (int or float)
- `b`: Divisor (int or float)

**Returns:** Result of a / b as a float

**Raises:**
- `TypeError`: If either argument is not a number
- `ZeroDivisionError`: If b is zero

**Examples:**
```python
divide(10, 2)   # 5.0
divide(10, 3)   # 3.3333333333333335
divide(10, -2)  # -5.0
```

## Type Support

- **Supported Types**: `int`, `float`
- **Unsupported Types**: `str`, `bool`, `None`, `list`, `dict`, complex numbers, `Decimal`

All functions perform strict type checking and will raise `TypeError` for invalid inputs.

## Floating-Point Precision

This module uses Python's built-in floating-point arithmetic (IEEE 754). Be aware of precision limitations:

```python
result = add(0.1, 0.2)
print(result)  # 0.30000000000000004 (not exactly 0.3)

# For comparisons, use tolerance:
assert abs(result - 0.3) < 1e-10  # Recommended
```

For exact decimal arithmetic, consider using Python's `decimal.Decimal` module.

## Error Handling

The module raises two types of exceptions:

- **`TypeError`**: Invalid argument type
  - Message: "Both arguments must be numbers (int or float)"

- **`ZeroDivisionError`**: Division by zero
  - Message: "Cannot divide by zero"

## Specification

For complete acceptance criteria and detailed behavioral specifications, see [spec.md](spec.md).

## Requirements

- Python 3.12 or higher (for `int | float` union syntax)

## Testing

Run tests using pytest:

```bash
pytest test_calculator.py
```

## License

MIT License

## Contributing

Contributions are welcome! Please ensure all acceptance criteria in [spec.md](spec.md) are met.
