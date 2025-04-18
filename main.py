import tkinter as tk
from calculator_app import CalculatorApp

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()