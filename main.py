import tkinter as tk

# main application; creating GUI and handles user inputs
class CalculatorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("ZetaOne")
        self.root.resizable(True, True)
        self.root.configure(bg="#262626")

        self.current_input = ""

        self.entry = tk.Entry(root, validate="key",
                              width=14, font=("Helvetica Neue", 30, "bold"), 
                              borderwidth=1, relief="solid", justify="right")
        self.entry.configure(bg="#595959", fg="#C04F15")
        self.entry.grid(row=0, column=0, columnspan=4)

        self.root.bind("<Key>", self.on_key_press) # Bind keys for input
        self.root.bind("<Control-v>", self.on_paste) # Bind Ctrl+V for paste


        # buttons for the calculator
        buttons = [
            "1", "2", "3", "/",
            "4", "5", "6", "*",
            "7", "8", "9", "-",
            "0", ".", "=", "+"
        ]

        row_val = 1
        col_val = 0

        # creating buttons
        for button_icon in buttons:
            button = tk.Button(root, text=button_icon, width=3, height=1, font=("Helvetica Neue", 24),
                               command=lambda char=button_icon: self.button_pressed(char))
            button.configure(bg="#262626", fg="#C04F15", activebackground="#595959",
                             activeforeground="#C04F15")
            button.grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

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

    def button_pressed(self, char) -> None:
        if char == "=":
            self.calculate_result()
        else:
            self.update_entry(char)
    
    def on_paste(self, event=None) -> None:
        try:
            text = self.root.clipboard_get()
            if all(c.isdigit() or c in "+-*/." for c in text):
                self.update_entry(text)
        except Exception:
            self.error("Invalid paste")

    def update_entry(self, text) -> None:
        self.current_input += text
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.current_input)

    def backspace(self) -> None:
        self.current_input = self.current_input[:-1]
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.current_input)
    
    def error(self, message) -> None:
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, message)
        
    def calculate_result(self) -> None:     
        user_input = self.current_input
        try:
            solution = eval(user_input)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(solution))
            self.current_input = str(solution)
        except ZeroDivisionError:
            self.error("Error: Division by zero")
        except Exception as e:
            self.error("Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()