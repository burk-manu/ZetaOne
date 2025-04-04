from sympy import sympify, pi, E, sin, cos, tan, log, sqrt

def evaluate(user_input: str) -> str:
        result = float(sympify(user_input).evalf())
        

        if abs(result - round(result)) < 1e-9:
            return str(int(round(result)))
        
        return str(result)