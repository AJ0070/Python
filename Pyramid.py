def print_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces before the asterisks
        for j in range(rows - i):
            print(" ", end="")
        
        # Print asterisks
        for k in range(2 * i - 1):
            print("*", end="")
        
        # Move to the next line
        print()

# Get the number of rows for the pyramid from the user
num_rows = input("Enter the number of rows for the pyramid: ")

# Convert the user input to an integer
try:
    num_rows = int(num_rows)
    print_pyramid(num_rows)
except ValueError:
    print("Invalid input. Please enter a valid number of rows.")
