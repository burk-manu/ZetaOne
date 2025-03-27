import tkinter as tk

# main application; creating GUI and habdles user inputs
class CalculatorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("ZetaOne")
        self.root.resizable(False, False)
        self.root.configure(bg="#262626")

        self.current_input = ""

        self.entry = tk.Entry(root, width=14, font=("Helvetica Neue", 30, "bold"), borderwidth=1, relief="solid",)
        self.entry.configure(bg="#595959", fg="#C04F15")
        self.entry.grid(row=0, column=0, columnspan=4)

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
            button = tk.Button(root, text=button_icon, width=3, height=1, font=("Helvetica Neue", 24), command=lambda char=button_icon: self.button_pressed(char))
            button.configure(bg="#262626", fg="#C04F15", activebackground="#595959", activeforeground="#C04F15")
            button.grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
        # binds the key press event to the entry
        self.root.bind("<Key>", self.key_pressed)

    # calculates the result of the user input and actualizes the entry
    def button_pressed(self, char) -> None:
        if char == "=":
            self.calculate_result()
        else:
            self.update_entry(char)
    
    def key_pressed(self, event) -> None:
        char = event.char
        if char == "\r":
            self.calculate_result()
        else:
            if self.entry != self.root.focus_get():
                if char == "\b":
                    self.entry.delete(len(self.entry.get())-1, tk.END)
                elif char.isdigit() or char in "+-*/.":
                    self.update_entry(char)

    def update_entry(self, text) -> None:
        self.current_input = self.entry.get()
        self.current_input += text
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, self.current_input)
        

    def calculate_result(self) -> None:     
        user_input = self.entry.get()
        if user_input == "1234":
            self.activate_easter_egg()
        else:
            try:
                solution = eval(user_input)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(solution))
            except ZeroDivisionError:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Division by zero")
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
    
    def activate_easter_egg(self):
        print("Easter Egg activated")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()