import random
import string

def generate_password(length, use_symbols=True):
    characters = string.ascii_letters + string.digits

    if use_symbols:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))