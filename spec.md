# Calculator Module Specification

Version: 1.0.0
Last Updated: 2026-01-06

## Overview

A basic calculator module providing four fundamental arithmetic operations for use by Python developers. This module prioritizes type safety, clear error messages, and predictable behavior across edge cases.

---

## User Stories

### Core Operations

**US-1: Addition**
As a developer integrating this calculator module,
I want to add two numbers together,
so that I can perform addition operations in my application without implementing the logic myself.

**US-2: Subtraction**
As a developer integrating this calculator module,
I want to subtract one number from another,
so that I can perform subtraction operations reliably in my application.

**US-3: Multiplication**
As a developer integrating this calculator module,
I want to multiply two numbers,
so that I can perform multiplication operations without writing custom logic.

**US-4: Division**
As a developer integrating this calculator module,
I want to divide one number by another,
so that I can perform division operations in my application.

### Error Handling & Usability

**US-5: Division by Zero Protection**
As a developer integrating this calculator module,
I want to receive a clear error when attempting to divide by zero,
so that I can handle this edge case gracefully in my application.

**US-6: Type Flexibility**
As a developer integrating this calculator module,
I want to work with both integers and floating-point numbers,
so that I can handle various numeric types without converting them manually.

**US-7: Type Safety**
As a developer integrating this calculator module,
I want to receive clear errors when passing invalid types,
so that I can catch programming errors early in development.

**US-8: Predictable API**
As a developer integrating this calculator module,
I want to use a simple and intuitive API,
so that I can quickly implement calculations without reading extensive documentation.

---

## Function Signatures

All functions use Python 3.12+ union type syntax (`int | float`).

```python
def add(a: int | float, b: int | float) -> int | float:
    """Add two numbers together."""

def subtract(a: int | float, b: int | float) -> int | float:
    """Subtract b from a (returns a - b)."""

def multiply(a: int | float, b: int | float) -> int | float:
    """Multiply two numbers."""

def divide(a: int | float, b: int | float) -> float:
    """Divide a by b (always returns float)."""
```

### Key Design Decisions

1. **Return Types**:
   - `add`, `subtract`, `multiply`: Return `int | float` (preserves input type when both are ints)
   - `divide`: Always returns `float` (even for 10 / 2 = 5.0)

2. **Parameter Order for `subtract(a, b)`**:
   - Returns `a - b`
   - Example: `subtract(5, 3)` returns `2` (not `3 - 5 = -2`)

3. **Type Validation**:
   - Explicit `isinstance` checks with clear error messages
   - Boolean values rejected (even though `bool` is a subclass of `int` in Python)

---

## Acceptance Criteria

### Addition (`add`)

#### Happy Path Scenarios

**AC-ADD-1: Integer Addition**
- GIVEN two positive integers `5` and `3`
- WHEN I call `add(5, 3)`
- THEN I should receive `8`

**AC-ADD-2: Float Addition**
- GIVEN two floating-point numbers `2.5` and `3.7`
- WHEN I call `add(2.5, 3.7)`
- THEN I should receive `6.2`

**AC-ADD-3: Mixed Type Addition**
- GIVEN an integer `5` and a float `2.5`
- WHEN I call `add(5, 2.5)`
- THEN I should receive `7.5`

#### Edge Cases

**AC-ADD-4: Addition with Zero**
- GIVEN a number `10` and zero `0`
- WHEN I call `add(10, 0)`
- THEN I should receive `10`

**AC-ADD-5: Addition with Negative Numbers**
- GIVEN a negative number `-5` and a positive number `3`
- WHEN I call `add(-5, 3)`
- THEN I should receive `-2`

**AC-ADD-6: Both Negative**
- GIVEN two negative numbers `-5` and `-3`
- WHEN I call `add(-5, -3)`
- THEN I should receive `-8`

**AC-ADD-7: Large Numbers**
- GIVEN two large numbers `1000000` and `2000000`
- WHEN I call `add(1000000, 2000000)`
- THEN I should receive `3000000`

**AC-ADD-8: IEEE 754 Floating-Point Precision**
- GIVEN `0.1` and `0.2`
- WHEN I call `add(0.1, 0.2)`
- THEN I should receive `0.30000000000000004` (not exactly `0.3`)
- AND the result should be within `1e-10` of `0.3` for practical comparison
- **Rationale**: Documents expected IEEE 754 binary representation behavior

**AC-ADD-9: Very Small Decimals**
- GIVEN two small decimals `0.1` and `0.2`
- WHEN I call `add(0.1, 0.2)`
- THEN the result should be approximately `0.3` within floating-point precision

---

### Subtraction (`subtract`)

#### Happy Path Scenarios

**AC-SUB-1: Integer Subtraction**
- GIVEN two positive integers `10` and `4`
- WHEN I call `subtract(10, 4)`
- THEN I should receive `6`

**AC-SUB-2: Integer Subtraction (Clarifying Example)**
- GIVEN integers `5` and `3`
- WHEN I call `subtract(5, 3)`
- THEN I should receive `2` (computed as 5 - 3)

**AC-SUB-3: Float Subtraction**
- GIVEN two floating-point numbers `7.5` and `2.3`
- WHEN I call `subtract(7.5, 2.3)`
- THEN I should receive `5.2`

**AC-SUB-4: Mixed Type Subtraction**
- GIVEN an integer `10` and a float `3.5`
- WHEN I call `subtract(10, 3.5)`
- THEN I should receive `6.5`

#### Edge Cases

**AC-SUB-5: Subtraction with Zero (a - 0)**
- GIVEN a number `10` and zero `0`
- WHEN I call `subtract(10, 0)`
- THEN I should receive `10`

**AC-SUB-6: Subtracting from Zero (0 - b)**
- GIVEN zero `0` and a number `5`
- WHEN I call `subtract(0, 5)`
- THEN I should receive `-5`

**AC-SUB-7: Subtracting Negative Number**
- GIVEN a number `5` and a negative number `-3`
- WHEN I call `subtract(5, -3)`
- THEN I should receive `8` (5 - (-3) = 5 + 3)

**AC-SUB-8: Both Negative**
- GIVEN two negative numbers `-5` and `-3`
- WHEN I call `subtract(-5, -3)`
- THEN I should receive `-2` (-5 - (-3) = -5 + 3)

**AC-SUB-9: Result is Negative**
- GIVEN a smaller number `3` and a larger number `10`
- WHEN I call `subtract(3, 10)`
- THEN I should receive `-7`

**AC-SUB-10: Large Numbers**
- GIVEN two large numbers `5000000` and `2000000`
- WHEN I call `subtract(5000000, 2000000)`
- THEN I should receive `3000000`

---

### Multiplication (`multiply`)

#### Happy Path Scenarios

**AC-MUL-1: Integer Multiplication**
- GIVEN two positive integers `6` and `7`
- WHEN I call `multiply(6, 7)`
- THEN I should receive `42`

**AC-MUL-2: Float Multiplication**
- GIVEN two floating-point numbers `2.5` and `4.0`
- WHEN I call `multiply(2.5, 4.0)`
- THEN I should receive `10.0`

**AC-MUL-3: Mixed Type Multiplication**
- GIVEN an integer `5` and a float `2.5`
- WHEN I call `multiply(5, 2.5)`
- THEN I should receive `12.5`

#### Edge Cases

**AC-MUL-4: Multiply by Zero**
- GIVEN a number `10` and zero `0`
- WHEN I call `multiply(10, 0)`
- THEN I should receive `0`

**AC-MUL-5: Multiply by One**
- GIVEN a number `10` and one `1`
- WHEN I call `multiply(10, 1)`
- THEN I should receive `10`

**AC-MUL-6: Multiply with Negative Number**
- GIVEN a positive number `5` and a negative number `-3`
- WHEN I call `multiply(5, -3)`
- THEN I should receive `-15`

**AC-MUL-7: Both Negative**
- GIVEN two negative numbers `-4` and `-5`
- WHEN I call `multiply(-4, -5)`
- THEN I should receive `20`

**AC-MUL-8: Large Numbers**
- GIVEN two large numbers `1000` and `2000`
- WHEN I call `multiply(1000, 2000)`
- THEN I should receive `2000000`

**AC-MUL-9: Small Decimals**
- GIVEN two small decimals `0.1` and `0.2`
- WHEN I call `multiply(0.1, 0.2)`
- THEN I should receive a value approximately equal to `0.02` (within floating-point precision)

---

### Division (`divide`)

#### Happy Path Scenarios

**AC-DIV-1: Integer Division (Exact)**
- GIVEN two integers `10` and `2`
- WHEN I call `divide(10, 2)`
- THEN I should receive `5.0` (float, not int)

**AC-DIV-2: Integer Division (with Remainder)**
- GIVEN two integers `10` and `3`
- WHEN I call `divide(10, 3)`
- THEN I should receive approximately `3.3333333333333335`

**AC-DIV-3: Float Division**
- GIVEN two floating-point numbers `7.5` and `2.5`
- WHEN I call `divide(7.5, 2.5)`
- THEN I should receive `3.0`

**AC-DIV-4: Mixed Type Division**
- GIVEN an integer `10` and a float `2.5`
- WHEN I call `divide(10, 2.5)`
- THEN I should receive `4.0`

#### Edge Cases

**AC-DIV-5: Divide Zero**
- GIVEN zero `0` and a number `5`
- WHEN I call `divide(0, 5)`
- THEN I should receive `0.0`

**AC-DIV-6: Divide by One**
- GIVEN a number `10` and one `1`
- WHEN I call `divide(10, 1)`
- THEN I should receive `10.0`

**AC-DIV-7: Negative Dividend**
- GIVEN a negative number `-10` and a positive number `2`
- WHEN I call `divide(-10, 2)`
- THEN I should receive `-5.0`

**AC-DIV-8: Negative Divisor**
- GIVEN a positive number `10` and a negative number `-2`
- WHEN I call `divide(10, -2)`
- THEN I should receive `-5.0`

**AC-DIV-9: Both Negative**
- GIVEN two negative numbers `-10` and `-2`
- WHEN I call `divide(-10, -2)`
- THEN I should receive `5.0`

**AC-DIV-10: Large Numbers**
- GIVEN two large numbers `1000000` and `2000`
- WHEN I call `divide(1000000, 2000)`
- THEN I should receive `500.0`

#### Error Cases

**AC-DIV-ERR-1: Division by Zero (Integer)**
- GIVEN a number `10` and zero `0`
- WHEN I call `divide(10, 0)`
- THEN a `ZeroDivisionError` should be raised
- AND the error message should be "Cannot divide by zero"

**AC-DIV-ERR-2: Division by Zero (Float)**
- GIVEN a float `5.5` and zero `0.0`
- WHEN I call `divide(5.5, 0.0)`
- THEN a `ZeroDivisionError` should be raised
- AND the error message should be "Cannot divide by zero"

---

### Type Validation (All Operations)

#### Error Cases

**AC-TYPE-ERR-1: String as First Parameter**
- GIVEN a string `"10"` and a number `5`
- WHEN I call any operation with `("10", 5)`
- THEN a `TypeError` should be raised
- AND the error message should be "Both arguments must be numbers (int or float)"

**AC-TYPE-ERR-2: String as Second Parameter**
- GIVEN a number `10` and a string `"5"`
- WHEN I call any operation with `(10, "5")`
- THEN a `TypeError` should be raised
- AND the error message should be "Both arguments must be numbers (int or float)"

**AC-TYPE-ERR-3: Both Parameters as Strings**
- GIVEN two strings `"10"` and `"5"`
- WHEN I call any operation with `("10", "5")`
- THEN a `TypeError` should be raised
- AND the error message should be "Both arguments must be numbers (int or float)"

**AC-TYPE-ERR-4: None as Parameter**
- GIVEN `None` and a number `5`
- WHEN I call any operation with `(None, 5)`
- THEN a `TypeError` should be raised
- AND the error message should be "Both arguments must be numbers (int or float)"

**AC-TYPE-ERR-5: List as Parameter**
- GIVEN a list `[1, 2, 3]` and a number `5`
- WHEN I call any operation with `([1, 2, 3], 5)`
- THEN a `TypeError` should be raised
- AND the error message should be "Both arguments must be numbers (int or float)"

**AC-TYPE-ERR-6: Boolean as Parameter**
- GIVEN a boolean `True` and a number `5`
- WHEN I call any operation with `(True, 5)`
- THEN a `TypeError` should be raised
- AND the error message should be "Both arguments must be numbers (int or float)"
- **Rationale**: Even though `bool` is a subclass of `int` in Python, we explicitly reject it to prevent confusing behavior

---

## Scope

### In Scope

- Four basic arithmetic operations: add, subtract, multiply, divide
- Support for `int` and `float` types
- Type validation with clear error messages
- Division by zero error handling
- IEEE 754 floating-point arithmetic behavior

### Out of Scope

- Complex numbers
- Decimal type support for exact decimal arithmetic
- Arbitrary precision arithmetic
- Mathematical operations beyond basic arithmetic (power, modulo, square root, etc.)
- Rounding or precision control
- Unit conversions
- Vector or matrix operations
- Stateful calculator (e.g., memory functions)
- Expression parsing (e.g., `calculate("2 + 3 * 4")`)
- Bitwise operations

---

## Error Handling

### Exception Types

| Exception | When Raised | Message Format |
|-----------|-------------|----------------|
| `TypeError` | Invalid argument type | "Both arguments must be numbers (int or float)" |
| `ZeroDivisionError` | Division by zero | "Cannot divide by zero" |

### Error Handling Philosophy

1. **Fail Fast**: Invalid inputs raise exceptions immediately
2. **Clear Messages**: Error messages describe the problem in plain language
3. **Type Strictness**: No implicit type coercion (e.g., `"5"` is not converted to `5`)
4. **No Silent Failures**: Never return `None` or sentinel values for errors

---

## Behavioral Notes

### Floating-Point Precision

This module uses Python's built-in floating-point arithmetic, which follows IEEE 754 standards. Key implications:

1. **Inexact Representation**: Some decimal values cannot be represented exactly
   - Example: `add(0.1, 0.2)` returns `0.30000000000000004`, not `0.3`

2. **Comparison Tolerance**: When comparing float results, use tolerance-based comparison
   ```python
   result = add(0.1, 0.2)
   assert abs(result - 0.3) < 1e-10  # Recommended
   # assert result == 0.3  # May fail!
   ```

3. **Alternative for Exact Decimals**: If exact decimal arithmetic is required, use Python's `decimal.Decimal` type (out of scope for this module)

### Return Type Preservation

- Operations on two integers may return an integer (add, subtract, multiply)
- Division ALWAYS returns a float, even for exact divisions: `divide(10, 2)` → `5.0`
- Operations involving at least one float always return a float

---

## Testing Strategy

### Test Coverage Requirements

1. **Happy Path**: All acceptance criteria marked "Happy Path"
2. **Edge Cases**: Zero, negatives, large numbers, small decimals
3. **Error Cases**: Type validation, division by zero
4. **Floating-Point Behavior**: IEEE 754 precision quirks

### Example Test Structure

```python
def test_add_integers():
    """AC-ADD-1: Integer Addition"""
    assert add(5, 3) == 8

def test_add_ieee754_precision():
    """AC-ADD-8: IEEE 754 Floating-Point Precision"""
    result = add(0.1, 0.2)
    assert result == 0.30000000000000004
    assert abs(result - 0.3) < 1e-10

def test_divide_by_zero_integer():
    """AC-DIV-ERR-1: Division by Zero (Integer)"""
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(10, 0)
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-06 | Initial specification |

---

## References

- [IEEE 754 Floating Point Standard](https://en.wikipedia.org/wiki/IEEE_754)
- [Python Type Hints (PEP 604)](https://peps.python.org/pep-0604/) - Union operator syntax
- [Python isinstance() Documentation](https://docs.python.org/3/library/functions.html#isinstance)
