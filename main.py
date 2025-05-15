# Author: Manuel Bürki
# Date: 2025-05-13
# License: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)
# Repository: https://github.com/XenovaStudios/ZetaOne

#main.py
import tkinter as tk
from calculator_app import CalculatorApp
import logging

def setup_logging():
    """
    Set up logging configuration.
    """
    logging.basicConfig(
        level=logging.DEBUG,  # Standard level; can later be reduced to DEBUG
        format="%(asctime)s %(levelname)-8s [%(name)s] %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

# Main function to run the calculator application
def main():
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Start calculator application")
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()