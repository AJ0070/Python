import tkinter as tk
from datetime import datetime

# Function to calculate age
def calculate_age():
    birth_year = int(entry_birth_year.get())
    current_year = datetime.now().year
    age = current_year - birth_year
    label_result.config(text=f"Your approximate age is: {age} years")

# Create the main application window
app = tk.Tk()
app.title("Age Predictor")

# Create and configure widgets
label_instructions = tk.Label(app, text="Enter your birth year:")
entry_birth_year = tk.Entry(app)
button_calculate = tk.Button(app, text="Calculate Age", command=calculate_age)
label_result = tk.Label(app, text="")

# Place widgets on the grid
label_instructions.grid(row=0, column=0, padx=10, pady=10)
entry_birth_year.grid(row=0, column=1, padx=10, pady=10)
button_calculate.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
label_result.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter main loop
app.mainloop()
