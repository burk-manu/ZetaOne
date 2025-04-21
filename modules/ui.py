# ui.py
from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from calculator_app import CalculatorApp


class CalculatorUI:
    def __init__(self, app: CalculatorApp) -> None:
        self.app = app
        self._init_entry()
        self._init_buttons()

    def _init_entry(self) -> None:
        entry = tk.Entry(
            self.app.root,
            font=("Helvetica Neue", 28, "bold"),
            borderwidth=1,
            relief="solid",
            justify="right"
        )
        entry.configure(bg="#262626", fg="#C04F15")
        entry.grid(row=0, column=0, columnspan=6, sticky="ew", padx=5, pady=5)
        entry.insert(tk.END, "0")
        self.app.entry = entry
        if not hasattr(self.app, 'entry') or self.app.entry is None:
            raise AttributeError("self.app.entry is not initialized properly.")

    def _init_buttons(self) -> None:
        layout = [
            ("MC", "MR", "M+", "M-", "C"),
            ("log", "ln", "|x|", "√", "^"),
            ("sin", "cos", "tan", "(", ")"),
            ("7", "8", "9", "/", "π"),
            ("4", "5", "6", "*", "e"),
            ("1", "2", "3", "-", "⌫"),
            ("0", ".", "±", "+", "="),
        ]
        for i, row in enumerate(layout):
            for j, text in enumerate(row):
                button = tk.Button(
                    self.app.root,
                    text=text,
                    width=3,
                    height=1,
                    font=("Helvetica Neue", 24),
                    bg="#262626",
                    fg="#C04F15",
                    activebackground="#262626",
                    activeforeground="#C04F15",
                    command=lambda t=text: self.button_pressed(t)
                )
                button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
                button_id = (f"0{i+1}" if i+1 < 10 else f"{i+1}") + (f"0{j+1}" if j+1 < 10 else f"{j+1}")
                self.app.buttons[button_id] = (text, button)

        for col in range(6):
            self.app.root.columnconfigure(col, weight=1)

    def button_pressed(self, char: str) -> None:
        if char == "=":
            self.app.evaluator.calculate_result()
        elif char == "C":
            self.app.ui.clear_entry()
        elif char == "⌫":
            self.app.ui.backspace()
        elif char == "±":
            self.toggle_sign()
        elif char in ("sin", "cos", "tan"):
            self.app.ui.update_entry(char + "(")
        else:
            self.app.ui.update_entry(char)
    
    def toggle_sign(self) -> None:
        try:
            self.app.ui.output(str(float(self.app.current_input)*(-1)))
        except Exception:
            self.app.ui.error("Error")
    
    def update_entry(self, text) -> None:
        result = self.app.evaluator.update_entry(text)
        self.app.current_input = result if result is not None else ""
        self.app.entry.delete(0, tk.END)
        self.app.entry.insert(tk.END, self.app.current_input)

    def backspace(self) -> None:
        self.app.current_input = self.app.current_input[:-1]
        self.app.entry.delete(0, tk.END)
        self.app.entry.insert(tk.END, self.app.current_input)

    def clear_entry(self) -> None:
        self.app.current_input = "0"
        self.app.entry.delete(0, tk.END)
        self.app.entry.insert(tk.END, "0")

    def output(self, text) -> None:
        self.app.entry.delete(0, tk.END)
        self.app.entry.insert(tk.END, text)
        self.app.current_input = text

    def error(self, message) -> None:
        self.app.entry.delete(0, tk.END)
        self.app.entry.insert(tk.END, message)

    def activate_secret_button(self) -> None:
        lock_btn = self.app.buttons.get("0705")
        if lock_btn is not None:
            lock_button = lock_btn[1]
            lock_button.configure(text="🔓", command=lambda: self.app.functions.easter_egg())
            self.app.root.after(2000, lambda: lock_button.configure(
                        text="=", 
                        command=lambda: self.button_pressed("=")
                    ))

    
    def change_theme(self) -> None:
        self.app.theme = "dark" if self.app.theme == "orange" else "orange"
        mode = self.app.theme
        self.app.root.configure(bg="#000000" if mode == "dark" else "#262626")
        self.app.entry.configure(bg="#000000" if mode == "dark" else "#262626", fg="#FF28C2" if mode == "dark" else "#C04F15")
        for id, (_, button) in self.app.buttons.items():
            background, foreground = self.button_color(id)
            button.configure(bg=background, fg=foreground, activebackground=background, activeforeground=foreground)
        
    def button_color(self, id: str) -> tuple[str, str]:
        mode = self.app.theme
        if id in ("0106", "0206", "0306", "0406", "0506", "0606", "0706"):
            return ("#000000", "#FF28C2") if mode == "dark" else ("#565656", "#C04F15")
        elif id in ("0701", "0702", "0703", "0601", "0602", "0603", "0501", "0502", "0503", "0401", "0402", "0403"): #("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "±")
            return ("#000000", "#4C58FF") if mode == "dark" else ("#262626", "#C04F15")
        elif id in ("0101", "0102", "0103", "0104", "0105", "0106", "0201", "0202", "0203", "0204", "0205", "0206", "0301", "0302", "0303", "0304", "0305", "0306", "0404", "0405", "0406", "0504", "0505", "0506", "0604", "0605", "0606", "0704"): #("MC", "MR", "M+", "M-", "C", "log", "ln", "|x|", "√", "^", "sin", "cos", "tan", "(", ")", "/", "*", "-", "+", "⌫", "π", "e")
            return ("#000000", "#02FFA6") if mode == "dark" else ("#262626", "#C04F15")
        elif id in ("0705"): #("=")
            return ("#000000", "#FF005D") if mode == "dark" else ("#262626", "#C04F15")

        else: # fallback to default color
            return ("#000000", "#FFFFFF") if mode == "dark" else ("#262626", "#C04F15")