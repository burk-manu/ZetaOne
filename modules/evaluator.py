# evaluator.py
from __future__ import annotations
from sympy import sympify, pi, E, log, Abs, rad
import re
from sympy.functions import sin, cos, tan
import logging
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from calculator_app import CalculatorApp


class Evaluator:
    def __init__(self, app: CalculatorApp) -> None:
        self.app = app

        self.logger = logging.getLogger(__name__)

    def prepare_input_for_calculation(self) -> str:
        """
        Prepares the user input for evaluation by replacing constants, operators,
        and converting trigonometric functions from radians to degrees.
        """
        user_input = self.app.current_input

        if user_input == "ZetaOne":
            self.app.ui.show_btn_for_advanced_options()
            return "0"

        # Replace constants and special characters
        user_input = self._replace_constants(user_input)

        # Replace trigonometric functions
        user_input = self._replace_trigonometric_functions(user_input)

        return user_input

    def _replace_constants(self, user_input: str) -> str:
        """
        Replaces constants like π and e, and operators like ^ with their equivalents.
        """
        replacements = {
            'π': pi,
            'e': E,
            '^': "**",
        }
        for symbol, value in replacements.items():
            user_input = user_input.replace(symbol, str(value))
        return user_input

    def _replace_trigonometric_functions(self, user_input: str) -> str:
        """
        Converts trigonometric functions from radians to degrees using sympy.
        """
        def replace_trig(match):
            func = match.group(1)
            try:
                value = float(match.group(2))
                degrees = rad(value)  # Convert degrees to radians
                return f"{func}({degrees})"
            except ValueError:
                self.app.ui.error("Error")
                return match.group(0)

        trig_pattern = r'\b(sin|cos|tan)\(\s*([+-]?\d*\.?\d+)\s*\)' # Matches sin(x), cos(x), tan(x)
        return re.sub(trig_pattern, replace_trig, user_input)

    def update_entry(self, text: str) -> str:
        """
        Updates the calculator's input entry with the given text.
        """
        pending_input = self.app.current_input + text

        # Remove leading zero if not followed by a decimal or operator
        if len(pending_input) > 1 and re.match(r"^0(?![.\+\-\*\/])", pending_input):
            pending_input = pending_input[1:]

        # Replace patterns like "\\pi " with their symbols
        replacements = {r"\\pi ": 'π'}
        for pattern, symbol in replacements.items():
            pending_input = re.sub(pattern, symbol, pending_input)

        return pending_input

    def calculate_operation(self, operation: str) -> None:
        """
        Performs a specific operation (e.g., sqrt, abs, log) on the user input.
        """
        try:
            user_input = self.prepare_input_for_calculation()
            result = None

            if operation == "sqrt":
                result = float(user_input) ** 0.5
            elif operation == "abs":
                result = Abs(float(user_input))
            elif operation in ("log", "ln"):
                result = self.calculate_logarithm(operation, user_input)
            else:
                self.app.ui.error("Error")
                return
            if type(result) is float:
                result = self.round_result(result)
                self.app.ui.output(result)
        except Exception as e:
            self.app.ui.error("Error")

    def calculate_logarithm(self, operation: str, user_input: str) -> float:
        """
        Calculates the logarithm (log or ln) of the user input.
        """
        try:
            if operation == "log":
                return float(log(sympify(user_input), 10).evalf())  # type: ignore # Base-10 logarithm
            elif operation == "ln":
                return float(log(sympify(user_input)).evalf())  # type: ignore # Natural logarithm
            else:
                self.app.ui.error("Error")
                self.logger.debug("Unsupported logarithm operation: %s", operation)
                raise ValueError(f"Unsupported logarithm operation: {operation}")
        except ValueError as e:
            self.app.ui.error("Error")
            self.logger.debug("Logarithm calculation error: %s", e)
            raise ValueError("Invalid input for logarithm calculation")
        

    def calculate_result(self) -> None:
        """
        Evaluates the user input and displays the result.
        """
        try:
            user_input = self.prepare_input_for_calculation()
            result = self.evaluate(user_input)
            self.app.ui.output(result)
        except Exception as e:
            self.app.ui.error("Error")
            self.logger.exception("Calculation error: %s", e)

    def evaluate(self, user_input: str) -> str:
        """
        Evaluates the prepared user input using sympy.
        """
        try:
            result = sympify(user_input).evalf()
            self.logger.debug("Evaluated result: %s", result)
            return self.round_result(result)
        except Exception as e:
            self.app.ui.error("Error")
            self.logger.exception("Evaluation error: %s", e)
            raise ValueError("Invalid input for evaluation")

    def round_result(self, result: float) -> str:
        """
        Rounds the result to an integer if it's very close to an integer.
        """
        if abs(result - round(result)) < 1e-9:
            self.logger.debug("Rounding result to integer: %s", result)
            return str(int(round(result)))
        self.logger.debug("Result was not rounded: %s", result)
        return str(result)