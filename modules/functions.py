# functions.py
from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from calculator_app import CalculatorApp

class Functions:

    def __init__(self, app:CalculatorApp) -> None:
        self.app = app

    def easter_egg(self):
        lock_btn = self.app.buttons.get("=")
        if lock_btn:
            lock_btn.configure(text="=", command=lambda: self.app.ui.button_pressed("="))
        pro_labels = ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]
        if not self.app.extra_shown:
            for i, label in enumerate(pro_labels):
                button = tk.Button(
                self.app.root,
                text=label,
                width=3,
                height=1,
                font=("Helvetica Neue", 24),
                bg=self.app.ui.button_color(label)[0],
                fg=self.app.ui.button_color(label)[1],
                activebackground="#565656",
                activeforeground="#C04F15",
                command=lambda lbl=label: self.pro_button(lbl))

                button.grid(row=i+1, column=5, padx=5, pady=5, sticky="nsew")
                self.app.buttons[label] = button

            self.app.extra_shown = True
        
        else:
            # destroy all pro‑buttons
            for label in list(self.app.buttons.keys()):
                if label in ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]:
                    self.app.buttons[label].destroy()
                    del self.app.buttons[label]
            self.app.extra_shown = False

        
    def pro_button(self, label):
        if label == "P1":
            self.app.ui.change_theme()
        elif label == "P2":
            self.app.ui.output("Pro button 2 pressed")
        elif label == "P3":
            self.app.ui.output("Pro button 3 pressed")
        elif label == "P4":
            self.app.ui.output("Pro button 4 pressed")
        elif label == "P5":
            self.app.ui.output("Pro button 5 pressed")
        elif label == "P6":
            self.app.ui.output("Pro button 6 pressed")
        elif label == "P7":
            self.app.ui.output("Pro button 7 pressed")