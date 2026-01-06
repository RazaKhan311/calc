"""
Basic calculator module with four operations: addition, subtraction, multiplication, and division.

This module provides simple arithmetic operations for use by other developers.
All functions accept integers and floats, and include proper type validation and error handling.
"""


def add(a: int | float, b: int | float) -> int | float:
    """
    Add two numbers together.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Sum of a and b

    Raises:
        TypeError: If either argument is not a number (int or float)

    Examples:
        >>> add(5, 3)
        8
        >>> add(2.5, 3.7)
        6.2
        >>> add(5, 2.5)
        7.5
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("Both arguments must be numbers (int or float)")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Both arguments must be numbers (int or float)")

    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """
    Subtract b from a.

    Args:
        a: Number to subtract from (int or float)
        b: Number to subtract (int or float)

    Returns:
        Result of a - b

    Raises:
        TypeError: If either argument is not a number (int or float)

    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(10, 4)
        6
        >>> subtract(3, 10)
        -7
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("Both arguments must be numbers (int or float)")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Both arguments must be numbers (int or float)")

    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """
    Multiply two numbers.

    Args:
        a: First number (int or float)
        b: Second number (int or float)

    Returns:
        Product of a and b

    Raises:
        TypeError: If either argument is not a number (int or float)

    Examples:
        >>> multiply(6, 7)
        42
        >>> multiply(2.5, 4.0)
        10.0
        >>> multiply(5, 2.5)
        12.5
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("Both arguments must be numbers (int or float)")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Both arguments must be numbers (int or float)")

    return a * b


def divide(a: int | float, b: int | float) -> float:
    """
    Divide a by b.

    Args:
        a: Dividend (int or float)
        b: Divisor (int or float)

    Returns:
        Result of a / b as a float

    Raises:
        TypeError: If either argument is not a number (int or float)
        ZeroDivisionError: If b is zero

    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(10, 3)
        3.3333333333333335
        >>> divide(7.5, 2.5)
        3.0
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("Both arguments must be numbers (int or float)")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("Both arguments must be numbers (int or float)")

    if b == 0 or b == 0.0:
        raise ZeroDivisionError("Cannot divide by zero")

    return a / b
