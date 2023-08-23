# Function to calculate BMI
def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

# Function to interpret BMI
def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 24.9 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# Input from the user
weight_kg = float(input("Enter your weight in kilograms: "))
height_m = float(input("Enter your height in meters: "))

# Calculate BMI
bmi = calculate_bmi(weight_kg, height_m)

# Interpret BMI
interpretation = interpret_bmi(bmi)

# Display the result
print(f"Your BMI is {bmi:.2f}")
print(f"You are categorized as: {interpretation}")
