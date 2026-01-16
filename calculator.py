"""
Calculator Module

A minimal, type-safe calculator providing four basic arithmetic operations.

Note: Uses `from __future__ import annotations` for Python 3.8+ compatibility
      with Python 3.10+ type hint syntax (int | float).

Functions:
    add: Return the sum of two numbers
    subtract: Return the difference of two numbers
    multiply: Return the product of two numbers
    divide: Return the quotient of two numbers
"""

from __future__ import annotations

import math


def _validate_operands(a: int | float, b: int | float) -> None:
    """Validate that both operands are int or float (not bool)."""
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Operands must be int or float")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Operands must be int or float")


def _check_nan(result: int | float) -> None:
    """Raise ValueError if result is NaN."""
    if isinstance(result, float) and math.isnan(result):
        raise ValueError("Result is undefined (NaN)")


def add(a: int | float, b: int | float) -> int | float:
    """Return the sum of a and b.

    Args:
        a: First operand (int or float)
        b: Second operand (int or float)

    Returns:
        Sum of a and b. Returns int if both inputs are int, otherwise float.

    Raises:
        TypeError: If either operand is not int or float.
        ValueError: If the result is NaN.

    Examples:
        >>> add(5, 3)
        8
        >>> add(5, 3.5)
        8.5
        >>> add(-5, 3)
        -2
    """
    _validate_operands(a, b)
    result = a + b
    _check_nan(result)
    return result


def subtract(a: int | float, b: int | float) -> int | float:
    """Return the difference of a minus b.

    Args:
        a: First operand (int or float)
        b: Second operand (int or float)

    Returns:
        Difference (a - b). Returns int if both inputs are int, otherwise float.

    Raises:
        TypeError: If either operand is not int or float.
        ValueError: If the result is NaN.

    Examples:
        >>> subtract(10, 4)
        6
        >>> subtract(10, 2.5)
        7.5
        >>> subtract(0, 7)
        -7
    """
    _validate_operands(a, b)
    result = a - b
    _check_nan(result)
    return result


def multiply(a: int | float, b: int | float) -> int | float:
    """Return the product of a and b.

    Args:
        a: First operand (int or float)
        b: Second operand (int or float)

    Returns:
        Product of a and b. Returns int if both inputs are int, otherwise float.

    Raises:
        TypeError: If either operand is not int or float.
        ValueError: If the result is NaN.

    Examples:
        >>> multiply(6, 7)
        42
        >>> multiply(4, 2.5)
        10.0
        >>> multiply(-4, -5)
        20
    """
    _validate_operands(a, b)
    result = a * b
    _check_nan(result)
    return result


def divide(a: int | float, b: int | float) -> float:
    """Return a divided by b.

    Args:
        a: Dividend (int or float)
        b: Divisor (int or float)

    Returns:
        Quotient as float. Always returns float, even for exact divisions.

    Raises:
        TypeError: If either operand is not int or float.
        ZeroDivisionError: If b is zero.
        ValueError: If the result is NaN.

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
        >>> divide(-10, -2)
        5.0
    """
    _validate_operands(a, b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    result = float(a) / float(b)
    _check_nan(result)
    # Normalize -0.0 to 0.0
    if result == 0.0:
        return 0.0
    return result
