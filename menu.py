import tkinter as tk
import os

def run_elements_script():
    os.system('python elements.py')

def run_radio_script():
    os.system('python radio.py')

# Create the main window
root = tk.Tk()
root.title("Script Runner")

# Create buttons to run the scripts
elements_button = tk.Button(root, text="Form Submission Test", command=run_elements_script)
elements_button.pack(pady=10)

radio_button = tk.Button(root, text="Radio Button Functionality", command=run_radio_script)
radio_button.pack(pady=10)

root.mainloop()