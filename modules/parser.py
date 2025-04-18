import re
from sympy import pi, E, sin, cos, tan, log, sqrt
from modules import functions
from modules import ui

# prepares user input for evaluation
def prepare_input_for_eval(app: str) -> str:
    user_input = app.current_input
    if user_input == "ZetaOne":
        lock_btn = app.buttons.get("=")
        if lock_btn:
            lock_btn.configure(text="🔓", command=lambda: functions.easter_egg(app))
            return "0"
    else:
        lock_btn = app.buttons.get("=")
        if lock_btn:
            lock_btn.configure(text="=", command=lambda: ui.button_pressed(app, "="))

        replacements = {
            'π': pi,
            'e': E,
            '^': "**",
        }
        for symbol, value in replacements.items():
            user_input = user_input.replace(symbol, str(value))
        
        return user_input

def update_entry(current_input, text):
    pending_input = current_input + text
    if len(pending_input) > 1 and re.match(r"^0(?![.\+\-\*\/])", pending_input):
        pending_input = pending_input[1:]

    replacements = {r"\\pi": 'π', r"\\e": 'e',}

    for pattern, symbol in replacements.items():
        pending_input = re.sub(pattern, symbol, pending_input)

    return pending_input