# functions.py
from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING
from modules.advanced_options import AdvancedOptions

if TYPE_CHECKING:
    from calculator_app import CalculatorApp

class Functions:

    def __init__(self, app:CalculatorApp) -> None:
        self.app = app
    
    def activate_advanced_options(self) -> None:
        """
        Activates the advanced options window.
        If the window is already open, it will be brought to the front.
        """
        if self.app.advanced_window is None or not self.app.advanced_window.winfo_exists():
            # Create a new window if it doesn't exist or has been destroyed
            self.app.advanced_window = tk.Toplevel(self.app.root)
            self.app.advanced_window.title("Advanced Options")
            self.app.advanced_window.resizable(False, False)
            self.app.advanced_window.configure(bg="#262626")
            self.app.advanced_window.protocol("WM_DELETE_WINDOW", self.close_advanced_options)
            AdvancedOptions(self.app, self.app.advanced_window)
        else:
            # Redisplay the window if minimized or hidden
            self.app.advanced_window.deiconify()
            self.app.advanced_window.lift()       
            self.app.advanced_window.focus_force()


    def close_advanced_options(self) -> None:
        """
        Closes the advanced options window and resets the reference in the app.
        """
        if self.app.advanced_window is not None:
            self.app.advanced_window.destroy()
            self.app.advanced_window = None