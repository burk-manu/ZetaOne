# keyboard.py
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from calculator_app import CalculatorApp

class Keyboard:
    def __init__(self, app: CalculatorApp) -> None:
        """
        Initializes the keyboard bindings for the calculator application.
        Binds key events to specific functions for handling user input.
        """
        self.app = app
        self.root = app.root
        self._init_keyboard()
        
    def _init_keyboard(self) -> None:
        """
        Binds keyboard events to their respective functions.
        """
        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<Control-v>", self.on_paste)
        self.root.bind("<Control-c>", self.on_copy)

    def on_key_press(self, event) -> None:
        """
        Defines the actions for key presses.
        Handles Enter, Backspace, and other character inputs.
        """
        char = event.char
        if char == "\r":
            self.app.evaluator.calculate_result()
        elif char == "\b":
            self.app.ui.backspace()
        else:
            self.app.ui.update_entry(char)

    def on_paste(self, event=None) -> None:
        """
        Retrieves text from the clipboard and updates the entry field.
        """
        try:
            text = self.root.clipboard_get()
            self.app.ui.update_entry(text)
        except Exception:
            self.app.ui.error("Invalid paste")

    def on_copy(self, event=None) -> None:
        """
        Copies the current input in the entry field to the clipboard.
        """
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.app.current_input)
        except Exception:
            self.app.ui.error("Invalid copy")