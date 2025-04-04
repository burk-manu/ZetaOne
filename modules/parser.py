import re
from sympy import sympify, pi, E, sin, cos, tan, log, sqrt

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