import tkinter as tk

def easter_egg(app):
    pro_labels = ["P1", "P2", "P3", "P4", "P5", "P6", "P7"]
    if not getattr(app, "extra_shown", False):
        for i, label in enumerate(pro_labels):
            button = tk.Button(
                app.root,
                text=label,
                width=3,
                height=1,
                font=("Helvetica Neue", 24),
                bg="#303030",
                fg="#FFFFFF",
                activebackground="#595959",
                activeforeground="#FFFFFF",
                command=lambda lbl=label: pro_button(app, lbl)
            )
            button.grid(row=i+1, column=5, padx=5, pady=5, sticky="nsew")
            app.pro_buttons[label] = button
            app.buttons[label] = button
        app.extra_shown = True
    else:
        # destroy all pro‑buttons
        for button in app.pro_buttons.values():
            button.destroy()
        app.pro_buttons.clear()
        app.extra_shown = False

def pro_button(app, label):
    print(f"{label} was pressed")