# calculator_app.py
import tkinter as tk
from modules.ui import CalculatorUI
from modules.keyboard import Keyboard
from modules.evaluator import Evaluator
from modules.functions import Functions
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from calculator_app import CalculatorApp

class CalculatorApp:

    def __init__(self, root):
        # type notations to prevent error in IDE
        self.root: tk.Tk
        self.entry: tk.Entry

        self.root = root
        self.root.title("ZetaOne")
        self.root.resizable(False, False)
        self.root.configure(bg="#262626")

        self.current_input = "0"
        self.buttons: dict[str, tuple[str, tk.Button]] = {}

        self.extra_shown = False
        self.pro_buttons = {}

        self.theme = "orange"

        self.ui = CalculatorUI(self)
        self.keyboard = Keyboard(self)
        self.evaluator = Evaluator(self)
        self.functions = Functions(self)