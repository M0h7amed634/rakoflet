import tkinter as tk
from math import sqrt

# Functionality for buttons
def on_button_click(value):
    if value == "C":
        entry.delete(0, tk.END)  # Clear the input
    elif value == "=":
        try:
            result = eval(entry.get())  # Evaluate the current input
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "√":
        try:
            result = sqrt(float(entry.get()))  # Calculate square root
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "^":
        try:
            result = float(entry.get()) ** 2  # Square the number
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, value)  # Add value to the input field


# Create the main window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")
window.resizable(False, False)

# Entry widget to display input and results
entry = tk.Entry(window, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Buttons layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3),
    ("√", 5, 0), ("^", 5, 1), ("=", 5, 2)
]

# Add buttons to the window
for text, row, col in buttons:
    button = tk.Button(window, text=text, font=("Arial", 18), bg="#4CAF50", fg="white",
                       padx=10, pady=10, command=lambda t=text: on_button_click(t))
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the main loop
window.mainloop()
