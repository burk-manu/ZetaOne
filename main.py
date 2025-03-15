import tkinter as tk

window = tk.Tk()
window.title("ZetaOne")

def calculate():
    user_input = entry.get()
    try:
        result = eval(user_input)
        label.config(text=f"Result: {result}")
    except ZeroDivisionError:
        label.config(text="an error occured")

entry = tk.Entry(window)
entry.pack()

label = tk.Label(window, text="Result:")
label.pack()

button = tk.Button(window, text="calculate", command=calculate)
button.pack()

window.mainloop()