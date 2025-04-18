import tkinter as tk
from modules import parser as pars
from modules import evaluator
from modules import functions
from modules import ui

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ZetaOne")
        self.root.resizable(False, False)
        self.root.configure(bg="#262626")

        self.current_input = "0"
        self.buttons = {}

        self.extra_shown = False
        self.pro_buttons = {}


        self.entry = tk.Entry(root, font=("Helvetica Neue", 30, "bold"),
                              borderwidth=1, relief="solid", justify="right")
        self.entry.configure(bg="#595959", fg="#C04F15")
        self.entry.grid(row=0, column=0, columnspan=6, sticky="ew", padx=5, pady=5)
        self.entry.insert(tk.END, "0")

        for c in range(6):
            self.root.columnconfigure(c, weight=1)

        self.root.bind("<Key>", self.on_key_press)
        self.root.bind("<Control-v>", self.on_paste)
        self.root.bind("<Control-c>", self.on_copy)

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
        self.check_input()

    def update_entry(self, text) -> None:
        self.current_input = pars.update_entry(self.current_input, text)
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.current_input)
        self.check_input()

    def backspace(self) -> None:
        self.current_input = self.current_input[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.current_input)
        self.check_input()

    def clear_entry(self) -> None:
        self.current_input = "0"
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, "0")
        self.check_input()

    def calculate_operation(self, operation) -> None:
        try:
            result = operation(float(self.current_input))
            self.output(str(result))
        except Exception:
            self.error("Error")

    def calculate_result(self) -> None:
        try:
            user_input = pars.prepare_input_for_eval(self.current_input)
            result = evaluator.evaluate(user_input)
            self.output(result)
        except Exception:
            self.error("Error")

    def output(self, text) -> None:
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, text)
        self.current_input = text

    def error(self, message) -> None:
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, message)

    def check_input(self) -> None:
        if self.current_input == "ZetaOne":
            lock_btn = self.buttons.get("=")
            if lock_btn:
                lock_btn.configure(text="🔓", command=lambda: functions.easter_egg(self))
        else:
            lock_btn = self.buttons.get("=")
            if lock_btn:
                lock_btn.configure(text="=", command=lambda: self.button_pressed("="))

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()