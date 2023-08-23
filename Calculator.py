# Take user input for the operation and numbers
x = float(input("Enter the first number: "))
z = input("Enter the operation (+, -, *, /): ")
y = float(input("Enter the second number: "))

# Perform the calculation based on the chosen operation
if z == '+':
    result = x + y
elif z == '-':
    result = x - y
elif z == '*':
    result = x * y
elif z == '/':
    if y != 0:  # Check for division by zero
        result = x / y
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

print("Result:", result)
