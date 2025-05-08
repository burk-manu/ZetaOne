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
        """
        Initializes the main Calculator application which includes all the modules.
        The modules can get accessed via the self.<module> variable.
        self is handed over to the modules to prevent circular imports.
        Modules access each other via the self.app.<module> variable. -> app is the self instance of the CalculatorApp class.
        """
        # type notations to prevent error in IDE
        self.root: tk.Tk
        self.entry: tk.Entry

        self.root = root
        self.root.title("ZetaOne")
        self.root.resizable(False, False)
        self.root.configure(bg="#262626")

        self.current_input = "0" # current input variable
        self.buttons: dict[str, tuple[str, tk.Button]] = {} # dictionary of all buttons including id, label and button object

        self.history = []

        # current theme
        self.theme = "orange"

        # Variables for the advanced options window
        self.advanced_window: tk.Toplevel = None
        self.extra_shown = False
        self.pro_buttons = {}

        # Initialize modules
        self.ui = CalculatorUI(self)
        self.keyboard = Keyboard(self)
        self.evaluator = Evaluator(self)
        self.functions = Functions(self)