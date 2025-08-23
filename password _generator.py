# Password Generator in Python
import random
import string

def generate_password(length=12):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure password has at least one of each (uppercase, lowercase, digit, special char)
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest with random choices
    password += random.choices(characters, k=length-4)
    
    # Shuffle to avoid predictable sequence
    random.shuffle(password)
    
    return "".join(password)

# User Input
try:
    length = int(input("Enter the desired password length (minimum 4): "))
    if length < 4:
        print("Password length must be at least 4 characters.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Invalid input! Please enter a number.")
