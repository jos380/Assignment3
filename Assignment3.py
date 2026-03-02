# Program Name: Assignment3.py
# Course: IT3883/Section XXX
# Student Name: John Doe
# Assignment Number: Lab 3
# Due Date: 03/10/20XX
# Purpose: 
# This program creates a GUI application that converts Miles Per Gallon (MPG)
# into Kilometers Per Liter (KM/L). The result updates automatically as the 
# user types. The program safely handles invalid input (letters or blank values)
# without crashing.
#
# Resources Used:
# - Class notes
# - Python Tkinter documentation (official Python docs)

import tkinter as tk

# Conversion constant
CONVERSION_FACTOR = 0.425143707


def convert_value(*args):
    """
    This function is triggered automatically whenever
    the user types in the MPG entry box.
    It converts MPG to KM/L and updates the result label.
    """
    user_input = mpg_variable.get()

    # If input box is empty, clear result
    if user_input.strip() == "":
        result_variable.set("")
        return

    try:
        # Try converting input to float
        mpg_value = float(user_input)

        # Perform conversion
        km_per_liter = mpg_value * CONVERSION_FACTOR

        # Display result rounded to 4 decimal places
        result_variable.set(f"{km_per_liter:.4f}")

    except ValueError:
        # If user types letters or invalid input
        result_variable.set("Invalid Input")


# Create main application window
main_window = tk.Tk()
main_window.title("MPG to KM/L Converter")
main_window.geometry("350x150")

# String variables to store user input and result
mpg_variable = tk.StringVar()
result_variable = tk.StringVar()

# Trace method calls convert_value automatically when input changes
mpg_variable.trace_add("write", convert_value)

# Labels and Entry fields
input_label = tk.Label(main_window, text="Miles Per Gallon (MPG):")
input_label.pack(pady=5)

mpg_entry = tk.Entry(main_window, textvariable=mpg_variable)
mpg_entry.pack(pady=5)

output_label = tk.Label(main_window, text="Kilometers Per Liter (KM/L):")
output_label.pack(pady=5)

result_display = tk.Label(main_window, textvariable=result_variable)
result_display.pack(pady=5)

# Run the GUI loop
main_window.mainloop()
