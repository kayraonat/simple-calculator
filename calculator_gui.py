import tkinter as tk
import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed!"
    return a / b

first_number = None
operation = None

def type_char(char):
    display.insert(tk.END, char)

def select_operation(new_operation):
    global first_number, operation
    try:
        first_number = float(display.get())
    except ValueError:
        return
    operation = new_operation
    display.delete(0, tk.END)

def calculate():
    global first_number, operation
    if first_number is None or operation is None:
        return
    try:
        second = float(display.get())
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")
        first_number = None
        operation = None
        return

    if operation == "+":
        result = add(first_number, second)
    elif operation == "-":
        result = subtract(first_number, second)
    elif operation == "*":
        result = multiply(first_number, second)
    elif operation == "/":
        result = divide(first_number, second)

    if isinstance(result, str):
        display.delete(0, tk.END)
        display.insert(0, result)
    else:
        if result == int(result):
            result = int(result)
        history.config(text=f"{first_number} {operation} {second} =")
        display.delete(0, tk.END)
        display.insert(0, result)

    first_number = None
    operation = None

def clear_all():
    global first_number, operation
    first_number = None
    operation = None
    display.delete(0, tk.END)
    history.config(text="")

def backspace():
    length = len(display.get())
    display.delete(length - 1, tk.END)

def square_root():
    try:
        value = float(display.get())
        result = math.sqrt(value)
        if result == int(result):
            result = int(result)
        display.delete(0, tk.END)
        display.insert(0, result)
    except (ValueError, OverflowError):
        display.delete(0, tk.END)
        display.insert(0, "Error")

def percent():
    try:
        value = float(display.get())
        display.delete(0, tk.END)
        display.insert(0, value / 100)
    except ValueError:
        display.delete(0, tk.END)
        display.insert(0, "Error")

window = tk.Tk()
window.title("Calculator")
window.geometry("300x440")

history = tk.Label(window, text="", anchor="e",
                   font=("Arial", 10), fg="gray")
history.grid(row=0, column=0, columnspan=4, sticky="ew", padx=5)

display = tk.Entry(window, width=20, font=("Arial", 20), justify="right")
display.grid(row=1, column=0, columnspan=4, pady=10)

buttons = [
    ("C", clear_all), ("⌫", backspace), ("√", square_root), ("%", percent),
    ("7", "7"), ("8", "8"), ("9", "9"), ("/", "/"),
    ("4", "4"), ("5", "5"), ("6", "6"), ("*", "*"),
    ("1", "1"), ("2", "2"), ("3", "3"), ("-", "-"),
    ("0", "0"), (".", "."), ("=", "="), ("+", "+"),
]

row, col = 2, 0
for button in buttons:
    text, command = button
    if text == "=":
        command = calculate
    elif not callable(command):
        if text in ["+", "-", "*", "/"]:
            command = (lambda m=text: select_operation(m))
        else:
            command = (lambda m=text: type_char(m))

    tk.Button(window, text=text, width=5, height=2,
              font=("Arial", 14), command=command
              ).grid(row=row, column=col, padx=3, pady=3)
    col += 1
    if col == 4:
        col = 0
        row += 1

window.mainloop()