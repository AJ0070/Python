import random
import string

def generate_password(length):
    # Define the character set for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Set the desired password length
password_length = int(input("Password Length: "))

# Generate and print a random password
random_password = generate_password(password_length)
print("Random Password:", random_password)
