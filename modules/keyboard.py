# keyboard.py
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from calculator_app import CalculatorApp

class Keyboard:
    def __init__(self, app: CalculatorApp) -> None:
        self.app = app
        self.root = app.root
        self._init_keyboard()
        
    def _init_keyboard(self) -> None:
        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<Control-v>", self.on_paste)
        self.root.bind("<Control-c>", self.on_copy)

    def on_key_press(self, event) -> None:
        char = event.char
        if char == "\r":
            self.app.evaluator.calculate_result()
        elif char == "\b":
            self.app.ui.backspace()
        else:
            self.app.ui.update_entry(char)

    def on_paste(self, event=None) -> None:
        try:
            text = self.root.clipboard_get()
            self.app.ui.update_entry(text)
        except Exception:
            self.app.ui.error("Invalid paste")

    def on_copy(self, event=None) -> None:
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.app.current_input)
        except Exception:
            self.app.ui.error("Invalid copy")