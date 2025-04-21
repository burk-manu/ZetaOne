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
        button_text_btn = self.app.buttons.get("0705")
        if button_text_btn is not None:
            lock_btn = button_text_btn[1]
            lock_btn.configure(text="=", command=lambda: self.app.ui.button_pressed("="))
        pro_labels = ["🏠", "P2", "P3", "P4", "P5", "P6", "P7"]
        if not self.app.extra_shown:
            for i, label in enumerate(pro_labels):
                button_id = f"0{i+1}06"
                button = tk.Button(
                self.app.root,
                text=label,
                width=3,
                height=1,
                font=("Helvetica Neue", 24),
                bg=self.app.ui.button_color(button_id)[0],
                fg=self.app.ui.button_color(button_id)[1],
                activebackground="#565656",
                activeforeground="#C04F15",
                command=lambda id=button_id: self.pro_button(id))

                button.grid(row=i+1, column=5, padx=5, pady=5, sticky="nsew")
                self.app.buttons[button_id] = (label, button)

            self.app.extra_shown = True
        
        else:
            # destroy all pro‑buttons
            for button_id in list(self.app.buttons.keys()):
                if button_id in ["0106", "0206", "0306", "0406", "0506", "0606", "0706"]:
                    self.app.buttons[button_id][1].destroy()
                    del self.app.buttons[button_id]
            self.app.extra_shown = False

        
    def pro_button(self, id: str) -> None:
        if id == "0106":
            self.app.ui.change_theme()
        elif id == "0206":
            self.app.ui.output("Pro button 2 pressed")
        elif id == "0306":
            self.app.ui.output("Pro button 3 pressed")
        elif id == "0406":
            self.app.ui.output("Pro button 4 pressed")
        elif id == "0506":
            self.app.ui.output("Pro button 5 pressed")
        elif id == "0606":
            self.app.ui.output("Pro button 6 pressed")
        elif id == "0706":
            self.app.ui.output("Pro button 7 pressed")