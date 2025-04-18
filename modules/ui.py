import tkinter as tk

def init_entry(app) -> None:
    app.entry = tk.Entry(app.root, font=("Helvetica Neue", 30, "bold"),
                            borderwidth=1, relief="solid", justify="right")
    app.entry.configure(bg="#595959", fg="#C04F15")
    app.entry.grid(row=0, column=0, columnspan=6, sticky="ew", padx=5, pady=5)
    app.entry.insert(tk.END, "0")


def init_buttons(app):
    buttons = [
    ("MC", "MR", "M+", "M-", "C"),
    ("log", "ln", "|x|", "√", "^"),
    ("sin", "cos", "tan", "(", ")"),
    ("7", "8", "9", "/", "π"),
    ("4", "5", "6", "*", "e"),
    ("1", "2", "3", "-", "="),
    ("0", ".", "±", "+", "⌫"),
    ]

    for i, row in enumerate(buttons):
        for j, text in enumerate(row):
            button = tk.Button(app.root, text=text, width=3, height=1, font=("Helvetica Neue", 24),
                            bg="#262626", fg="#C04F15",
                            activebackground="#595959", activeforeground="#C04F15",
                            command=lambda t=text: button_pressed(app, t))
            button.grid(row=i+1, column=j, padx=5, pady=5, sticky="nsew")
            app.buttons[text] = button
    
    for c in range(6):
        app.root.columnconfigure(c, weight=1)

def button_pressed(app, char) -> None:
    if char == "=":
        app.calculate_result()
    elif char == "C":
        app.clear_entry()
    elif char == "⌫":
        app.backspace()
    elif char == "±":
        app.toggle_sign()
    elif char in ["sin", "cos", "tan"]:
        app.update_entry(char + "(")
    else:
        app.update_entry(char)