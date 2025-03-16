import tkinter as tk

# main application; creating GUI and habdles user inputs
class CalculatorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("ZetaOne")

        self.entry = tk.Entry(root)
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
            button = tk.Button(root, text=button_icon, width=5, height=2, font=("Arial", 14),
                               command=lambda char=button_icon: self.button_pressed(char))
            button.grid(row=row_val, column=col_val, padx=5, pady=5)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

    # calculates the result of the user input and actualizes the entry
    def button_pressed(self, char):
        if char == "=":
            try:
                solution = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(solution))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        else:
            self.entry.insert(tk.END, char)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()