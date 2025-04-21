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
                self.app.buttons[text] = button

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
            self.app.ui.output(str(float(self.app.current_input)))
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
        lock_btn = self.app.buttons.get("=")
        if lock_btn:
            lock_btn.configure(text="🔓", command=lambda: self.app.functions.easter_egg())
            self.app.root.after(2000, lambda: lock_btn.configure(
                        text="=", 
                        command=lambda: self.button_pressed("=")
                    ))

    
    def change_theme(self) -> None:
        self.app.theme = "dark" if self.app.theme == "orange" else "orange"
        mode = self.app.theme
        self.app.root.configure(bg="#000000" if mode == "dark" else "#262626")
        self.app.entry.configure(bg="#000000" if mode == "dark" else "#262626", fg="#FF28C2" if mode == "dark" else "#C04F15")
        for label, button in self.app.buttons.items():
            background, foreground = self.button_color(label)
            button.configure(bg=background, fg=foreground, activebackground=background, activeforeground=foreground)
        
    def button_color(self, label: str) -> tuple[str, str]:
        mode = self.app.theme
        if label in ("P1", "P2", "P3", "P4", "P5", "P6", "P7"):
            return ("#000000", "#FF28C2") if mode == "dark" else ("#565656", "#C04F15")
        elif label in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "±"):
            return ("#000000", "#4C58FF") if mode == "dark" else ("#262626", "#C04F15")
        elif label in ("MC", "MR", "M+", "M-", "C", "log", "ln", "|x|", "√", "^", "sin", "cos", "tan", "(", ")", "/", "*", "-", "+", "⌫", "🔓", "π", "e"):
            return ("#000000", "#02FFA6") if mode == "dark" else ("#262626", "#C04F15")
        elif label in ("="):
            return ("#000000", "#FF005D") if mode == "dark" else ("#262626", "#C04F15")

        else: # fallback to default color
            return ("#000000", "#FFFFFF") if mode == "dark" else ("#262626", "#C04F15")