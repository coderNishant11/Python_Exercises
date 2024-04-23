# Develop a simple password generator program.


import random
import string

def generate_password(length=8):
    """Generate a random password of given length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password_length = 10  # You can change this to generate passwords of different lengths
generated_password = generate_password(password_length)
print("Generated Password:", generated_password)
