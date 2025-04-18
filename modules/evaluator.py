from sympy import sympify

def evaluate(app) -> str:
    user_input = app.user_input_for_calculation
    if user_input != "ZetaOne":
        result = float(sympify(user_input).evalf())

        if abs(result - round(result)) < 1e-9:
            return str(int(round(result)))
        
        return str(result)
    return "0"