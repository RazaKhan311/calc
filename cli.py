#!/usr/bin/env python3
"""
Calculator CLI

Usage:
    python cli.py                     # Interactive mode
    python cli.py add 5 3             # Single operation
    python cli.py subtract 10 4
    python cli.py multiply 6 7
    python cli.py divide 15 2
"""

from __future__ import annotations

import sys
from calculator import add, subtract, multiply, divide


OPERATIONS = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def parse_number(s: str) -> int | float:
    """Parse a string to int or float."""
    try:
        if '.' in s or 'e' in s.lower():
            return float(s)
        return int(s)
    except ValueError:
        raise ValueError(f"Invalid number: {s}")


def run_once(op: str, a: str, b: str) -> None:
    """Run a single calculation."""
    if op not in OPERATIONS:
        print(f"Unknown operation: {op}")
        print(f"Available: {', '.join(OPERATIONS.keys())}")
        sys.exit(1)

    try:
        num_a = parse_number(a)
        num_b = parse_number(b)
        result = OPERATIONS[op](num_a, num_b)
        print(result)
    except (TypeError, ZeroDivisionError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


def interactive_mode() -> None:
    """Run calculator in interactive mode."""
    print("Calculator - Interactive Mode")
    print("Commands: add, subtract, multiply, divide (or +, -, *, /)")
    print("Type 'quit' or 'q' to exit\n")

    while True:
        try:
            line = input("calc> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            break

        if not line:
            continue

        if line.lower() in ('quit', 'q', 'exit'):
            print("Goodbye!")
            break

        parts = line.split()

        if len(parts) != 3:
            print("Usage: <operation> <number> <number>")
            print("Example: add 5 3")
            continue

        op, a, b = parts

        if op not in OPERATIONS:
            print(f"Unknown operation: {op}")
            print(f"Available: add, subtract, multiply, divide (or +, -, *, /)")
            continue

        try:
            num_a = parse_number(a)
            num_b = parse_number(b)
            result = OPERATIONS[op](num_a, num_b)
            print(f"= {result}")
        except (TypeError, ZeroDivisionError, ValueError) as e:
            print(f"Error: {e}")


def main() -> None:
    if len(sys.argv) == 1:
        interactive_mode()
    elif len(sys.argv) == 4:
        _, op, a, b = sys.argv
        run_once(op, a, b)
    else:
        print("Usage:")
        print("  python cli.py                  # Interactive mode")
        print("  python cli.py <op> <a> <b>     # Single operation")
        print()
        print("Operations: add, subtract, multiply, divide (or +, -, *, /)")
        print()
        print("Examples:")
        print("  python cli.py add 5 3")
        print("  python cli.py divide 10 2")
        sys.exit(1)


if __name__ == "__main__":
    main()
