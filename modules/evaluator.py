# evaluator.py
from __future__ import annotations
from sympy import sympify
import re
from sympy import pi, E
from modules import functions
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from calculator_app import CalculatorApp

class Evaluator:
    def __init__(self, app: CalculatorApp) -> None:
        self.app = app
        self.root = app.root
    
    def prepare_input_for_calculation(self) -> str:
        user_input = self.app.current_input
        if user_input == "ZetaOne":
            self.app.ui.activate_secret_button()
            return "0"
        else:
            replacements = {
                'π': pi,
                'e': E,
                '^': "**",
            }
            for symbol, value in replacements.items():
                user_input = user_input.replace(symbol, str(value))
            
            return user_input
    
    def update_entry(self, text: str) -> str:
        pending_input = self.app.current_input + text
        if len(pending_input) > 1 and re.match(r"^0(?![.\+\-\*\/])", pending_input):
            pending_input = pending_input[1:]

        replacements = {r"\\pi ": 'π'}

        for pattern, symbol in replacements.items():
            pending_input = re.sub(pattern, symbol, pending_input)

        return pending_input
    
    def calculate_operation(self, operation) -> None:
        try:
            result = operation(float(self.app.current_input))
            self.app.ui.output(str(result))
        except Exception:
            self.app.ui.error("Error")

    def calculate_result(self) -> None:
        try:
            self.user_input_for_calculation = self.app.evaluator.prepare_input_for_calculation()
            result = self.app.evaluator.evaluate()
            self.app.ui.output(result)
        except ZeroDivisionError:
            self.app.ui.error("Error")
    
    def evaluate(self) -> str:
        user_input = self.app.evaluator.user_input_for_calculation
        if user_input != "ZetaOne":
            result = float(sympify(user_input).evalf())

            if abs(result - round(result)) < 1e-9:
                return str(int(round(result)))
            
            return str(result)
        return "0"