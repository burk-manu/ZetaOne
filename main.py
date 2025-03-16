import tkinter as tk


class CalculatorApp:

    def __init__(self, root):
        self.root = root
        self.root.title("ZetaOne")

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.label = tk.Label(root, text="Result:")
        self.label.pack()

        self.button = tk.Button(root, text="calculate", command=self.calculate)
        self.button.pack()

    def calculate(self):
        user_input = self.entry.get()
        try:
            result = eval(user_input)
            self.label.config(text=f"Result: {result}")
        except ZeroDivisionError:
            self.label.config(text="an error occured")


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()