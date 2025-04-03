import tkinter as tk
from math import pi, e, sin, cos, tan, log, sqrt
# main application; creating GUI and handles user inputs
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ZetaOne")
        self.root.resizable(False, False)
        self.root.configure(bg="#262626")

        self.current_input = ""

        self.entry = tk.Entry(root, validate="key",
                              width=16, font=("Helvetica Neue", 30, "bold"), 
                              borderwidth=1, relief="solid", justify="right")
        self.entry.configure(bg="#595959", fg="#C04F15")
        self.entry.grid(row=0, column=0, columnspan=4)

        self.root.bind("<Key>", self.on_key_press) # Bind keys for input
        self.root.bind("<Control-v>", self.on_paste) # Bind Ctrl+V for paste


        # buttons for the calculator
        buttons = [
            ("MC", "MR", "M+", "M-", "C"),
            ("log", "ln", "|x|", "√", "^"),
            ("sin", "cos", "tan", "(", ")"),
            ("7", "8", "9", "/", "π"),
            ("4", "5", "6", "*", "e"),
            ("1", "2", "3", "-", "="),
            ("0", ".", "±", "+", "⌫"),
        ]

        # create buttons and add them to the grid
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                button = tk.Button(root, text=text, width=3, height=1, font=("Helvetica Neue", 24),
                                   command=lambda t=text: self.button_pressed(t))
                button.configure(bg="#262626", fg="#C04F15", activebackground="#595959",
                                 activeforeground="#C04F15")
                button.grid(row=i + 1, column=j, padx=5, pady=5)

    # function to handle button presses
    def button_pressed(self, char) -> None:
        if char == "=":
            self.calculate_result()
        elif char == "C":
            self.clear_entry()
        elif char == "⌫":
            self.backspace()
        elif char == "π":
            self.update_entry(str(pi))
        elif char == "e":
            self.update_entry(str(e))
        elif char == "^":
            self.update_entry("**")
        else:
            self.update_entry(char)

    # function to handle key presses
    def on_key_press(self, event) -> None:
        char = event.char
        if char == "\r":
            self.calculate_result()
        elif char == "\b":
            self.backspace()
        elif char.isdigit() or char in "+-*/.":
            self.update_entry(char)
        elif (event.state & 0x4) and (event.keysym.lower() == 'v'):
            try:
                text = self.root.clipboard_get()
                if text.isdigit() or text in "+-*/.":
                    self.update_entry(text)
            except Exception as e:
                print(f"Error pasting clipboard content: {e}")
    
    # function to make paste inputs possible
    def on_paste(self, event=None) -> None: # handles paste
        try:
            text = self.root.clipboard_get()
            if all(c.isdigit() or c in "+-*/." for c in text):
                self.update_entry(text)
        except Exception:
            self.error("Invalid paste")

    # appends the current text to the entry and displays it
    def update_entry(self, text) -> None:
        self.current_input += text
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.current_input)

    # deletes the last character of the current input
    def backspace(self) -> None:
        self.current_input = self.current_input[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.current_input)
    
    # clears the current input and resets it to "0"
    def clear_entry(self) -> None:
        self.current_input = "0"
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, "0")    
    
    # function to handle mathematical operations
    def calculate_operation(self, operation) -> None:
        try:
            result = operation(float(self.current_input))
            self.output(str(result))
        except Exception as e:
            self.error("Error")

    # evaluates the current input and displays the result
    def calculate_result(self) -> None:     
        user_input = self.current_input
        try:
            result = eval(user_input)
            self.output(str(result))
        except ZeroDivisionError:
            self.error("Error: Division by zero")
        except Exception as e:
            self.error("Error")
    
    # function to print the result or another output
    def output(self, text) -> None:
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, text)
        self.current_input = text
    
    # displays an error message without changing the current input
    def error(self, message) -> None:
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()