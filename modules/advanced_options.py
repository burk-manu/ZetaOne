# adcanced_options.py
from __future__ import annotations
import tkinter as tk
import logging
from config.colors import BG_BLACK, BG_DARKGREY, BG_LIGHTGREY, FG_ORANGE, FG_WHITE, FG_BLUE, FG_GREEN, FG_RED, FG_PINK
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from calculator_app import CalculatorApp


class AdvancedOptions:

    def __init__(self, app: CalculatorApp, root: tk.Toplevel) -> None:
        """
        Initialize the AdvancedOptions class with the main app and root window.
        """
        self.app = app
        self.root = root
        root.title("Advanced Options")
        root.resizable(False, False)
        root.configure(bg=BG_DARKGREY)
        self.advanced_options()

        self.logger = logging.getLogger(__name__)
    
    
    def advanced_options(self):
        """
        Create the advanced options window with buttons and labels.
        """
        pro_labels = [("🏠", "P2"), ("P3", "P4"), ("P5", "P6"), ("P7", "P8")]
        if not self.app.extra_shown:
            for i, row in enumerate(pro_labels):
                for j, text in enumerate(row):
                    button_id = f"E-0{i+1}0{j+1}"
                    button = tk.Button(
                        self.root,
                        text=text,
                        width=3,
                        height=1,
                        font=("Helvetica Neue", 24),
                        bg=self.app.ui.button_color(button_id)[0],
                        fg=self.app.ui.button_color(button_id)[1],
                        activebackground=BG_LIGHTGREY,
                        activeforeground=FG_ORANGE,
                        command=lambda id=button_id: self.pro_button_pressed(id)
                    )
                    button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
                    self.app.buttons[button_id] = (text, button)

            self.app.extra_shown = True
        
        else:
            # destroy all pro‑buttons
            for button_id in list(self.app.buttons.keys()):
                if button_id in ["E-0101", "E-0201", "E-0301", "E-0401", "E-0501", "E-0601", "E-0701", "E-0801"]:
                    self.app.buttons[button_id][1].destroy()
                    del self.app.buttons[button_id]
            self.app.extra_shown = False

        
    def pro_button_pressed(self, id: str) -> None:
        """
        Define the actions for each button in the advanced options window.
        """
        if id == "E-0101":
            self.app.ui.change_theme()
        elif id == "E-0102":
            self.app.ui.output("P2 pressed")
        elif id == "E-0201":
            self.app.ui.output("P3 pressed")
        elif id == "E-0202":
            self.app.ui.output("P4 pressed")
        elif id == "E-0301":
            self.app.ui.output("P5 pressed")
        elif id == "E-0302":
            self.app.ui.output("P6 pressed")
        elif id == "E-0401":
            self.app.ui.output("P7 pressed")
        elif id == "E-0402":
            self.app.ui.output("P8 pressed")