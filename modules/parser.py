import re
from sympy import pi, E, sin, cos, tan, log, sqrt

# prepares user input for evaluation
def prepare_input_for_eval(user_input: str) -> str:
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

    return pending_input
        
