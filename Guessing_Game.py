import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Set the initial number of attempts
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

while True:
    try:
        # Get the user's guess
        guess = int(input("Take a guess: "))
        
        # Increment the number of attempts
        attempts += 1

        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number between 1 and 100.")

# End of the game
print("Thanks for playing!")
