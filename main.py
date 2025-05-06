# Author: Manuel Bürki
# Date: 2025-04-20
# License: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)

#main.py
import tkinter as tk
from calculator_app import CalculatorApp

# Main function to run the calculator application
def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()