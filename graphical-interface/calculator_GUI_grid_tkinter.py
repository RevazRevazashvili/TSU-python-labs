# გამოსადეგი ბმულები

# https://realpython.com/python-gui-tkinter/

import tkinter as tk

# Create the main window
window = tk.Tk()

# Create and configure the entry widget
input_txt = tk.Entry(window, width=29, bg="black", fg="white", font="bold", justify='right')
input_txt.pack(fill=tk.X, padx=5, pady=5)
input_txt.insert(tk.END, '0')

# Define functions for button actions
def append_to_entry(text):
    current_text = input_txt.get()
    if current_text == '0':
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, text)
    else:
        input_txt.insert(tk.END, text)

def clear_entry():
    input_txt.delete(0, tk.END)
    input_txt.insert(tk.END, '0')

def delete_last_char():
    current_text = input_txt.get()
    if len(current_text) > 1:
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, current_text[:-1])
    else:
        clear_entry()

def calculate_percentage():
    try:
        current_text = input_txt.get()
        result = float(current_text) / 100
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, str(result))
    except ValueError:
        clear_entry()

def calculate_inverse():
    try:
        current_text = input_txt.get()
        result = 1 / float(current_text)
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, str(result))
    except ValueError:
        clear_entry()

def calculate_square():
    try:
        current_text = input_txt.get()
        result = float(current_text) ** 2
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, str(result))
    except ValueError:
        clear_entry()

def calculate_square_root():
    try:
        current_text = input_txt.get()
        result = float(current_text) ** 0.5
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, str(result))
    except ValueError:
        clear_entry()

def append_operator(operator):
    current_text = input_txt.get()
    if not current_text[-1] in '+-*/':
        input_txt.insert(tk.END, f" {operator} ")

def calculate_result():
    try:
        expression = input_txt.get()
        result = eval(expression)
        input_txt.delete(0, tk.END)
        input_txt.insert(tk.END, str(result))
    except (SyntaxError, ZeroDivisionError, ValueError):
        clear_entry()

def append_decimal():
    current_text = input_txt.get()
    if '.' not in current_text.split()[-1]:
        input_txt.insert(tk.END, '.')

# Define a dictionary to map buttons to their functions
button_functions = {
    '%': calculate_percentage,
    'CE': clear_entry,
    'C': clear_entry,
    'del': delete_last_char,
    '1/x': calculate_inverse,
    'x^2': calculate_square,
    'sqrt(x)': calculate_square_root,
    '/': lambda: append_operator('/'),
    '*': lambda: append_operator('*'),
    '-': lambda: append_operator('-'),
    '+': lambda: append_operator('+'),
    '=': calculate_result,
    '.': append_decimal,
}

# Create the frame to hold the buttons
all_buttons = tk.Frame(window, padx=10, pady=5, bg="black")
all_buttons.pack(fill=tk.BOTH, expand=True)

# Configure the layout
for i in range(6):
    all_buttons.rowconfigure(i, weight=1)
    all_buttons.columnconfigure(i, weight=1)

# Define button labels
cal_buttons = [
    "%", "CE", "C", "del", "1/x", "x^2", "sqrt(x)", "/",
    "7", "8", "9", "*", "4", "5", "6", "-",
    "1", "2", "3", "+", "+-", "0", ".", "="
]

# Create and place the buttons
counter = 0
for i in range(6):
    for j in range(4):
        button_text = cal_buttons[counter]
        button = tk.Button(
            all_buttons, text=button_text, padx=5, pady=5, bg="#006400", fg="white", font="bold"
        )
        button.grid(row=i, column=j, sticky="nsew")
        if button_text.isdigit() or button_text == '.':
            button.bind("<Button-1>", lambda e, text=button_text: append_to_entry(text))
        else:
            button.bind("<Button-1>", lambda e, func=button_functions.get(button_text, lambda: None): func())
        counter += 1

window.mainloop()
