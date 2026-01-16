#!/usr/bin/env python3
"""
Calculator GUI Application

A simple graphical calculator using Tkinter.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk, messagebox
from calculator import add, subtract, multiply, divide


class CalculatorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x400")
        self.root.resizable(False, False)
        self.root.configure(bg="#2b2b2b")

        # Current expression and display value
        self.expression = ""
        self.current_input = ""
        self.first_number: float | None = None
        self.operation: str | None = None

        self._create_widgets()

    def _create_widgets(self):
        # Display frame
        display_frame = tk.Frame(self.root, bg="#2b2b2b")
        display_frame.pack(fill=tk.X, padx=10, pady=10)

        # Expression label (shows the ongoing calculation)
        self.expr_label = tk.Label(
            display_frame,
            text="",
            font=("SF Pro Display", 14),
            fg="#888888",
            bg="#2b2b2b",
            anchor="e"
        )
        self.expr_label.pack(fill=tk.X)

        # Main display
        self.display = tk.Entry(
            display_frame,
            font=("SF Pro Display", 36, "bold"),
            fg="#ffffff",
            bg="#2b2b2b",
            bd=0,
            justify="right",
            state="readonly"
        )
        self.display.pack(fill=tk.X, pady=(5, 0))
        self._update_display("0")

        # Buttons frame
        buttons_frame = tk.Frame(self.root, bg="#2b2b2b")
        buttons_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Button layout
        buttons = [
            ("C", 0, 0, "#a5a5a5", "#000000"),
            ("±", 0, 1, "#a5a5a5", "#000000"),
            ("%", 0, 2, "#a5a5a5", "#000000"),
            ("÷", 0, 3, "#ff9f0a", "#ffffff"),
            ("7", 1, 0, "#333333", "#ffffff"),
            ("8", 1, 1, "#333333", "#ffffff"),
            ("9", 1, 2, "#333333", "#ffffff"),
            ("×", 1, 3, "#ff9f0a", "#ffffff"),
            ("4", 2, 0, "#333333", "#ffffff"),
            ("5", 2, 1, "#333333", "#ffffff"),
            ("6", 2, 2, "#333333", "#ffffff"),
            ("−", 2, 3, "#ff9f0a", "#ffffff"),
            ("1", 3, 0, "#333333", "#ffffff"),
            ("2", 3, 1, "#333333", "#ffffff"),
            ("3", 3, 2, "#333333", "#ffffff"),
            ("+", 3, 3, "#ff9f0a", "#ffffff"),
            ("0", 4, 0, "#333333", "#ffffff", 2),  # colspan 2
            (".", 4, 2, "#333333", "#ffffff"),
            ("=", 4, 3, "#ff9f0a", "#ffffff"),
        ]

        # Configure grid
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)

        # Create buttons
        for btn_data in buttons:
            text = btn_data[0]
            row = btn_data[1]
            col = btn_data[2]
            bg = btn_data[3]
            fg = btn_data[4]
            colspan = btn_data[5] if len(btn_data) > 5 else 1

            btn = tk.Button(
                buttons_frame,
                text=text,
                font=("SF Pro Display", 20),
                fg=fg,
                bg=bg,
                activebackground=self._lighten_color(bg),
                activeforeground=fg,
                bd=0,
                highlightthickness=0,
                command=lambda t=text: self._on_button_click(t)
            )
            btn.grid(
                row=row,
                column=col,
                columnspan=colspan,
                sticky="nsew",
                padx=2,
                pady=2
            )

    def _lighten_color(self, hex_color: str) -> str:
        """Lighten a hex color for button press effect."""
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        r = min(255, r + 40)
        g = min(255, g + 40)
        b = min(255, b + 40)
        return f"#{r:02x}{g:02x}{b:02x}"

    def _update_display(self, value: str):
        """Update the main display."""
        self.display.configure(state="normal")
        self.display.delete(0, tk.END)
        self.display.insert(0, value)
        self.display.configure(state="readonly")

    def _on_button_click(self, button: str):
        """Handle button clicks."""
        if button.isdigit():
            self._handle_digit(button)
        elif button == ".":
            self._handle_decimal()
        elif button in ("+", "−", "×", "÷"):
            self._handle_operation(button)
        elif button == "=":
            self._handle_equals()
        elif button == "C":
            self._handle_clear()
        elif button == "±":
            self._handle_negate()
        elif button == "%":
            self._handle_percent()

    def _handle_digit(self, digit: str):
        if self.current_input == "0":
            self.current_input = digit
        else:
            self.current_input += digit
        self._update_display(self.current_input)

    def _handle_decimal(self):
        if "." not in self.current_input:
            if self.current_input == "":
                self.current_input = "0"
            self.current_input += "."
            self._update_display(self.current_input)

    def _handle_operation(self, op: str):
        if self.current_input:
            if self.first_number is not None and self.operation:
                self._calculate()
            else:
                self.first_number = float(self.current_input)
            self.current_input = ""

        self.operation = op
        op_symbol = {"÷": "÷", "×": "×", "−": "−", "+": "+"}[op]
        self.expr_label.config(text=f"{self._format_number(self.first_number)} {op_symbol}")

    def _handle_equals(self):
        if self.first_number is not None and self.operation and self.current_input:
            self._calculate()
            self.expr_label.config(text="")
            self.operation = None

    def _calculate(self):
        try:
            second_number = float(self.current_input)
            op_map = {
                "+": add,
                "−": subtract,
                "×": multiply,
                "÷": divide,
            }

            result = op_map[self.operation](self.first_number, second_number)
            self.first_number = result
            self.current_input = self._format_number(result)
            self._update_display(self.current_input)

        except ZeroDivisionError:
            self._update_display("Error")
            self.current_input = ""
            self.first_number = None
            self.operation = None
            self.expr_label.config(text="Cannot divide by zero")
        except (TypeError, ValueError) as e:
            self._update_display("Error")
            self.current_input = ""
            self.first_number = None
            self.operation = None
            self.expr_label.config(text=str(e))

    def _handle_clear(self):
        self.current_input = ""
        self.first_number = None
        self.operation = None
        self.expr_label.config(text="")
        self._update_display("0")

    def _handle_negate(self):
        if self.current_input and self.current_input != "0":
            if self.current_input.startswith("-"):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = "-" + self.current_input
            self._update_display(self.current_input)

    def _handle_percent(self):
        if self.current_input:
            value = float(self.current_input) / 100
            self.current_input = self._format_number(value)
            self._update_display(self.current_input)

    def _format_number(self, num: float | None) -> str:
        """Format a number for display."""
        if num is None:
            return "0"
        if num == int(num):
            return str(int(num))
        return str(num)


def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
