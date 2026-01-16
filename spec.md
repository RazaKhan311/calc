# Calculator Module Specification

> A minimal, type-safe Python calculator module for developers.

**Version:** 1.0.0
**Python:** 3.12+
**License:** MIT

---

## Table of Contents

1. [Overview](#overview)
2. [User Stories](#user-stories)
3. [API Specification](#api-specification)
4. [Acceptance Criteria](#acceptance-criteria)
5. [Design Decisions](#design-decisions)
6. [Out of Scope](#out-of-scope)

---

## Overview

This module provides four basic arithmetic operations as pure functions:

- `add(a, b)` — Addition
- `subtract(a, b)` — Subtraction
- `multiply(a, b)` — Multiplication
- `divide(a, b)` — Division

### Design Principles

1. **Explicit over implicit** — Errors raise exceptions, never return silent `None` or `nan`
2. **Type predictability** — Return types follow Python's native arithmetic rules
3. **Zero dependencies** — Pure Python, no external packages
4. **Testable** — Every behavior has concrete, verifiable examples

---

## User Stories

### Core Operations

**Addition**
> As a developer, I want to add two numbers together, so that I can compute sums without implementing arithmetic logic myself.

**Subtraction**
> As a developer, I want to subtract one number from another, so that I can calculate differences in my application.

**Multiplication**
> As a developer, I want to multiply two numbers, so that I can compute products for calculations like pricing or scaling.

**Division**
> As a developer, I want to divide one number by another, so that I can calculate ratios, averages, or distribute values evenly.

### Error Handling

**Division by Zero**
> As a developer, I want to receive a clear error when dividing by zero, so that I can handle this edge case gracefully in my application.

**Invalid Types**
> As a developer, I want clear errors when passing invalid types, so that I can debug type mismatches quickly.

### Usability

**Consistent Interface**
> As a developer, I want all operations to follow the same function signature pattern, so that the API is predictable and easy to learn.

**Decimal Support**
> As a developer, I want operations to work with both integers and decimals, so that I can perform precise calculations.

**Negative Numbers**
> As a developer, I want operations to handle negative numbers correctly, so that I can use the calculator for a full range of mathematical operations.

---

## API Specification

### Function Signatures

```python
def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of a and b."""

def subtract(a: int | float, b: int | float) -> int | float:
    """Return the difference of a minus b."""

def multiply(a: int | float, b: int | float) -> int | float:
    """Return the product of a and b."""

def divide(a: int | float, b: int | float) -> float:
    """Return a divided by b. Always returns float."""
```

### Return Type Rules

| Operation | Input Types | Return Type |
|-----------|-------------|-------------|
| `add` | `int, int` | `int` |
| `add` | `int, float` or `float, float` | `float` |
| `subtract` | `int, int` | `int` |
| `subtract` | `int, float` or `float, float` | `float` |
| `multiply` | `int, int` | `int` |
| `multiply` | `int, float` or `float, float` | `float` |
| `divide` | any valid | `float` (always) |

### Exceptions

| Exception | Raised When | Message |
|-----------|-------------|---------|
| `TypeError` | Non-numeric operand | `"Operands must be int or float"` |
| `ZeroDivisionError` | Division by zero | `"Cannot divide by zero"` |
| `ValueError` | Operation produces `nan` | `"Result is undefined (NaN)"` |

---

## Acceptance Criteria

### Addition: `add(a, b)`

#### Happy Path
- **GIVEN** two positive integers `5` and `3`
- **WHEN** I call `add(5, 3)`
- **THEN** I receive `8`

#### Type Handling
- **GIVEN** an integer `5` and a float `3.5`
- **WHEN** I call `add(5, 3.5)`
- **THEN** I receive `8.5` as a float

- **GIVEN** two floats `2.5` and `3.5`
- **WHEN** I call `add(2.5, 3.5)`
- **THEN** I receive `6.0`

#### Edge Cases
- **GIVEN** zero and a positive number `7`
- **WHEN** I call `add(0, 7)`
- **THEN** I receive `7`

- **GIVEN** two negative numbers `-5` and `-3`
- **WHEN** I call `add(-5, -3)`
- **THEN** I receive `-8`

- **GIVEN** a negative and positive number `-5` and `3`
- **WHEN** I call `add(-5, 3)`
- **THEN** I receive `-2`

- **GIVEN** two large numbers `1e15` and `1e15`
- **WHEN** I call `add(1e15, 1e15)`
- **THEN** I receive `2e15`

#### Error Cases
- **GIVEN** a string `"5"` and an integer `3`
- **WHEN** I call `add("5", 3)`
- **THEN** I receive a `TypeError` with message `"Operands must be int or float"`

---

### Subtraction: `subtract(a, b)`

#### Happy Path
- **GIVEN** two positive integers `10` and `4`
- **WHEN** I call `subtract(10, 4)`
- **THEN** I receive `6`

#### Type Handling
- **GIVEN** an integer `10` and a float `2.5`
- **WHEN** I call `subtract(10, 2.5)`
- **THEN** I receive `7.5` as a float

- **GIVEN** two floats `5.5` and `2.5`
- **WHEN** I call `subtract(5.5, 2.5)`
- **THEN** I receive `3.0`

#### Edge Cases
- **GIVEN** a number `7` and zero
- **WHEN** I call `subtract(7, 0)`
- **THEN** I receive `7`

- **GIVEN** zero and a number `7`
- **WHEN** I call `subtract(0, 7)`
- **THEN** I receive `-7`

- **GIVEN** two equal numbers `5` and `5`
- **WHEN** I call `subtract(5, 5)`
- **THEN** I receive `0`

- **GIVEN** two negative numbers `-5` and `-3`
- **WHEN** I call `subtract(-5, -3)`
- **THEN** I receive `-2`

- **GIVEN** two large numbers `1e15` and `1e14`
- **WHEN** I call `subtract(1e15, 1e14)`
- **THEN** I receive `9e14`

#### Error Cases
- **GIVEN** a list `[5]` and an integer `3`
- **WHEN** I call `subtract([5], 3)`
- **THEN** I receive a `TypeError` with message `"Operands must be int or float"`

---

### Multiplication: `multiply(a, b)`

#### Happy Path
- **GIVEN** two positive integers `6` and `7`
- **WHEN** I call `multiply(6, 7)`
- **THEN** I receive `42`

#### Type Handling
- **GIVEN** an integer `4` and a float `2.5`
- **WHEN** I call `multiply(4, 2.5)`
- **THEN** I receive `10.0` as a float

- **GIVEN** two floats `2.5` and `4.0`
- **WHEN** I call `multiply(2.5, 4.0)`
- **THEN** I receive `10.0`

#### Edge Cases
- **GIVEN** any number `42` and zero
- **WHEN** I call `multiply(42, 0)`
- **THEN** I receive `0`

- **GIVEN** any number `7` and one
- **WHEN** I call `multiply(7, 1)`
- **THEN** I receive `7`

- **GIVEN** a positive `5` and negative `-3`
- **WHEN** I call `multiply(5, -3)`
- **THEN** I receive `-15`

- **GIVEN** two negative numbers `-4` and `-5`
- **WHEN** I call `multiply(-4, -5)`
- **THEN** I receive `20`

- **GIVEN** two large numbers `1e10` and `1e10`
- **WHEN** I call `multiply(1e10, 1e10)`
- **THEN** I receive `1e20`

- **GIVEN** two small floats `0.1` and `0.2`
- **WHEN** I call `multiply(0.1, 0.2)`
- **THEN** I receive approximately `0.02` (within floating-point precision)

#### Error Cases
- **GIVEN** `None` and an integer `3`
- **WHEN** I call `multiply(None, 3)`
- **THEN** I receive a `TypeError` with message `"Operands must be int or float"`

---

### Division: `divide(a, b)`

#### Happy Path
- **GIVEN** two positive integers `10` and `2`
- **WHEN** I call `divide(10, 2)`
- **THEN** I receive `5.0` as a float

- **GIVEN** integers that don't divide evenly `7` and `2`
- **WHEN** I call `divide(7, 2)`
- **THEN** I receive `3.5`

#### Type Handling
- **GIVEN** an integer `10` and a float `2.5`
- **WHEN** I call `divide(10, 2.5)`
- **THEN** I receive `4.0`

- **GIVEN** two floats `7.5` and `2.5`
- **WHEN** I call `divide(7.5, 2.5)`
- **THEN** I receive `3.0`

#### Edge Cases
- **GIVEN** zero and a positive number `5`
- **WHEN** I call `divide(0, 5)`
- **THEN** I receive `0.0`

- **GIVEN** a negative and positive number `-10` and `2`
- **WHEN** I call `divide(-10, 2)`
- **THEN** I receive `-5.0`

- **GIVEN** two negative numbers `-10` and `-2`
- **WHEN** I call `divide(-10, -2)`
- **THEN** I receive `5.0`

- **GIVEN** a small number `1e-10` and large number `1e10`
- **WHEN** I call `divide(1e-10, 1e10)`
- **THEN** I receive `1e-20`

- **GIVEN** a number divided by itself `42` and `42`
- **WHEN** I call `divide(42, 42)`
- **THEN** I receive `1.0`

#### Error Cases
- **GIVEN** any number `10` and zero `0`
- **WHEN** I call `divide(10, 0)`
- **THEN** I receive a `ZeroDivisionError` with message `"Cannot divide by zero"`

- **GIVEN** a string `"10"` and an integer `2`
- **WHEN** I call `divide("10", 2)`
- **THEN** I receive a `TypeError` with message `"Operands must be int or float"`

---

## Design Decisions

### 1. Floating Point Precision

**Decision:** Accept IEEE 754 behavior (no rounding)

```python
add(0.1, 0.2)  # Returns 0.30000000000000004, NOT 0.3
```

**Rationale:**
- Matches Python's native behavior—no surprises for developers
- Performance is not degraded
- Precision-critical applications should use `decimal.Decimal` explicitly

**Contract:** This module uses native Python floats (IEEE 754). For exact decimal arithmetic, use `decimal.Decimal` before calling these functions.

---

### 2. Division by Zero

**Decision:** Raise `ZeroDivisionError`

```python
divide(10, 0)   # Raises ZeroDivisionError("Cannot divide by zero")
divide(0, 0)    # Raises ZeroDivisionError("Cannot divide by zero")
```

**Alternatives rejected:**

| Option | Problem |
|--------|---------|
| Return `float('inf')` | Mathematically incorrect (limit ≠ value) |
| Return `float('nan')` | Silent failure, propagates invisibly |
| Return `None` | Breaks type contract, causes downstream errors |

**Rationale:** Explicit errors over silent failures. Callers can catch and handle.

---

### 3. Type Preservation

**Decision:** Follow Python's native arithmetic rules

```python
add(5, 3)       # → 8 (int)
add(5, 3.0)     # → 8.0 (float)
divide(6, 2)    # → 3.0 (always float)
```

**Rules:**
- `int` op `int` → `int` (except division)
- `int` op `float` → `float`
- `float` op `float` → `float`
- `divide()` → always `float`

**Rationale for division always returning float:**
- `divide(7, 2)` must return `3.5`, not `3`
- Consistent return type simplifies caller code
- Matches Python 3's `/` operator behavior

---

### 4. Zero Behavior

**Mathematical properties preserved:**

| Operation | Zero's Role | Example |
|-----------|-------------|---------|
| Addition | Identity | `add(x, 0) → x` |
| Subtraction | Right identity | `subtract(x, 0) → x` |
| Multiplication | Absorbing | `multiply(x, 0) → 0` |
| Division | Zero numerator OK | `divide(0, x) → 0.0` |
| Division | Zero denominator | `ZeroDivisionError` |

**Signed zero normalization:**
```python
divide(0, -5)  # → 0.0, NOT -0.0
```

---

### 5. Negative Number Handling

**Decision:** Standard mathematical sign rules

| Expression | Result | Rule |
|------------|--------|------|
| `multiply(-5, -3)` | `15` | negative × negative = positive |
| `multiply(-5, 3)` | `-15` | negative × positive = negative |
| `divide(-10, -2)` | `5.0` | negative ÷ negative = positive |
| `divide(-10, 2)` | `-5.0` | negative ÷ positive = negative |

---

### 6. Large Number Limits

**Python's number system:**

| Type | Range | Overflow |
|------|-------|----------|
| `int` | Unlimited | Never |
| `float` | ±1.8e308 | → `inf` |

**Decision:** Allow `inf` as result, raise on `nan`

```python
# Overflow to infinity - allowed
multiply(1e200, 1e200)  # → inf

# Operations producing nan - raise ValueError
add(float('inf'), float('-inf'))    # → ValueError
multiply(float('inf'), 0)           # → ValueError
divide(float('inf'), float('inf'))  # → ValueError
```

**Rationale:**
- `inf` is a valid IEEE 754 value with defined arithmetic
- `nan` indicates undefined state—should not propagate silently

---

## Out of Scope

The following are explicitly **not** supported:

| Feature | Reason |
|---------|--------|
| Complex numbers | Use Python's `complex` type directly |
| Arbitrary precision decimals | Use `decimal.Decimal` |
| Chained operations | Compose function calls: `add(add(1, 2), 3)` |
| In-place modification | Pure functions only |
| Operator overloading | Module provides functions, not a class |
| Rounding utilities | Use Python's `round()` on results |
| Unit conversions | Outside arithmetic scope |
| Expression parsing | Use `ast.literal_eval` or a parser library |

---

## Quick Reference

```python
from calc import add, subtract, multiply, divide

# Basic usage
add(5, 3)           # → 8
subtract(10, 4)     # → 6
multiply(6, 7)      # → 42
divide(15, 2)       # → 7.5

# Type handling
add(5, 3.0)         # → 8.0 (float)
divide(6, 2)        # → 3.0 (always float)

# Error handling
try:
    divide(10, 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## Why This Is a Good Specification

1. **User-Centric** — Starts with user stories explaining why features exist
2. **Type-Explicit** — Clear signatures with Python 3.12+ union types
3. **Edge-Case Complete** — Documents all "gotcha" behaviors
4. **Testable** — Concrete GIVEN/WHEN/THEN scenarios, not prose descriptions
5. **Scoped** — Explicitly states what's out of scope
6. **Unambiguous** — No room for interpretation (e.g., "division always returns float")
