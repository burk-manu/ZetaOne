import tkinter as tk
from modules import parser as pars, evaluator, functions, ui

class CalculatorApp:
    root: tk.Tk
    entry: tk.Entry
    buttons: dict[str, tk.Button]
    current_input: str

    def __init__(self, root):
        self.root = root
        self.root.title("ZetaOne")
        self.root.resizable(False, False)
        self.root.configure(bg="#262626")

        self.current_input = "0"
        self.buttons = {}

        self.extra_shown = False
        self.pro_buttons = {}

        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<Control-v>", self.on_paste)
        self.root.bind("<Control-c>", self.on_copy)

        ui.init_entry(self)
        ui.init_buttons(self)

    def on_key_press(self, event) -> None:
        char = event.char
        if char == "\r":
            self.calculate_result()
        elif char == "\b":
            self.backspace()
        elif (event.state & 0x4) and (event.keysym.lower() == 'v'):
            try:
                text = self.root.clipboard_get()
                if text.isdigit() or text in "+-*/.":
                    self.update_entry(text)
            except Exception as e:
                print(f"Error pasting clipboard content: {e}")
        else:
            self.update_entry(char)

    def toggle_sign(self) -> None:
        try:
            self.output(str(-float(self.current_input)))
        except Exception:
            self.error("Error")

    def on_paste(self, event=None) -> None:
        try:
            text = self.root.clipboard_get()
            if all(c.isdigit() or c in "+-*/." for c in text):
                self.update_entry(text)
        except Exception:
            self.error("Invalid paste")

    def on_copy(self, event=None) -> None:
        try:
            self.root.clipboard_clear()
            self.root.clipboard_append(self.current_input)
        except Exception:
            self.error("Invalid copy")

    def update_entry(self, text) -> None:
        self.current_input = pars.update_entry(self.current_input, text)
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.current_input)

    def backspace(self) -> None:
        self.current_input = self.current_input[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.current_input)

    def clear_entry(self) -> None:
        self.current_input = "0"
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, "0")

    def calculate_operation(self, operation) -> None:
        try:
            result = operation(float(self.current_input))
            self.output(str(result))
        except Exception:
            self.error("Error")

    def calculate_result(self) -> None:
        try:
            self.user_input_for_calculation = pars.prepare_input_for_eval(self)
            result = evaluator.evaluate(self)
            self.output(result)
        except ZeroDivisionError:
            self.error("Error")

    def output(self, text) -> None:
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, text)
        self.current_input = text

    def error(self, message) -> None:
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, message)