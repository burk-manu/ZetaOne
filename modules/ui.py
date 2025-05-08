# ui.py
from __future__ import annotations
import tkinter as tk
from tkinter import messagebox
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from calculator_app import CalculatorApp


class CalculatorUI:
    def __init__(self, app: CalculatorApp) -> None:
        """
        Initializes the UI components of the calculator application.
        """
        self.app = app
        self._init_entry()
        self._init_buttons()

    def _init_entry(self) -> None:
        """
        Initializes the entry field for the calculator.
        """
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
        """
        Initialize and create the buttons for the calculator
        """
        layout = [
            ("📋", "📥", "exp", "🔒", "C"),
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
        """
        Handles button presses and performs the corresponding action.
        """
        if char == "=":
            self.app.evaluator.calculate_result()
        elif char == "📋":
            self.app.keyboard.on_copy()
        elif char == "📥":
            self.app.keyboard.on_paste()
        elif char == "exp":
            self.app.ui.update_entry("E")
        elif char == "🔒":
            self.app.ui.show_messagebox("This feature is not available yet.", "info")
        elif char == "C":
            self.app.ui.clear_entry()
        elif char == "⌫":
            self.app.ui.backspace()
        elif char == "±":
            self.toggle_sign()
        elif char in ("sin", "cos", "tan"):
            self.app.ui.update_entry(char + "(")
        elif char == "log":
            self.app.evaluator.calculate_operation("log")
        elif char == "ln":
            self.app.evaluator.calculate_operation("ln")
        elif char == "√":
            self.app.evaluator.calculate_operation("sqrt")
        elif char == "|x|":
            self.app.evaluator.calculate_operation("abs")
        else:
            self.app.ui.update_entry(char)
    
    def toggle_sign(self) -> None:
        """
        Toggles the sign of the current input in the entry field.
        """
        try:
            self.app.ui.output(str(float(self.app.current_input)*(-1)))
        except Exception:
            self.app.ui.error("Error")
    
    def update_entry(self, text) -> None:
        """
        Updates the entry field with the given text.
        """
        result = self.app.evaluator.update_entry(text)
        self.app.current_input = result if result is not None else ""
        self.app.entry.delete(0, tk.END)
        self.app.entry.insert(tk.END, self.app.current_input)

    def backspace(self) -> None:
        """
        Removes the last character from the current input in the entry field.
        """
        self.app.current_input = self.app.current_input[:-1]
        self.app.entry.delete(0, tk.END)
        self.app.entry.insert(tk.END, self.app.current_input)

    def clear_entry(self) -> None:
        """
        Clears the entry field and resets the current input to "0".
        """
        self.app.current_input = "0"
        self.app.entry.delete(0, tk.END)
        self.app.entry.insert(tk.END, "0")

    def output(self, text) -> None:
        """
        Displays the result in the entry field.
        """
        self.app.entry.delete(0, tk.END)
        self.app.entry.insert(tk.END, text)
        self.app.current_input = text

    def error(self, message) -> None:
        """
        Displays an error message in the entry field.
        Doesn't change the input in the current input variable.
        """
        self.app.entry.delete(0, tk.END)
        self.app.entry.insert(tk.END, message)

    def show_btn_for_advanced_options(self) -> None:
        """
        Shows a button to activate advanced options if the user agrees.
        """
        answer = self.app.ui.show_dialog_messagebox("Do you want to activate advanced options?", "askokcancel", "Dev Options")
        if answer == True:
            lock_btn = self.app.buttons.get("0104")
            if lock_btn is not None:
                lock_button = lock_btn[1]
                lock_button.configure(text="☰", command=lambda: self.app.functions.activate_advanced_options())
    
    def show_messagebox(self, message: str, type: str = "info", title: str = "") -> None:
        """
        Displays a message box with the given message and type.
        """
        if title == "":
            title = type
        if type == "info":
            messagebox.showinfo(title, message)
        elif type == "error":
            messagebox.showerror(title, message)
        elif type == "warning":
            messagebox.showwarning(title, message)            
        else:
            raise ValueError("Invalid message type. Use 'info', 'error', or 'warning'.")
        
    def show_dialog_messagebox(self, message: str, type: str = "askyesno", title: str = "") -> Union[str, bool]:
        """
        Displays a dialog message box with the given message and type.
        Returns the user's response.
        """
        if title == "":
            title = "Confirmation"
        if type == "askyesno":
            return messagebox.askyesno(title, message)
        elif type == "askokcancel":
            return messagebox.askokcancel(title, message)
        elif type == "askretrycancel":
            return messagebox.askretrycancel(title, message)
        elif type == "askyesnocancel":
            return messagebox.askyesnocancel(title, message)
        else:
            raise ValueError("Invalid message type.")
    
    def change_theme(self) -> None:
        """
        Toggles the theme of the calculator between dark and orange mode.
        """
        self.app.theme = "dark" if self.app.theme == "orange" else "orange"
        mode = self.app.theme
        self.app.root.configure(bg="#000000" if mode == "dark" else "#262626")
        self.app.entry.configure(bg="#000000" if mode == "dark" else "#262626", fg="#FF28C2" if mode == "dark" else "#C04F15")
        for id, (_, button) in self.app.buttons.items():
            background, foreground = self.button_color(id)
            button.configure(bg=background, fg=foreground, activebackground=background, activeforeground=foreground)
        
    def button_color(self, id: str) -> tuple[str, str]:
        """
        Returns the background and foreground color for a button based on its ID.
        """
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