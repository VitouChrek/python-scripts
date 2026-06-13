import secrets
import string


def generate_secure_password(length=20):
    # 1. Define the pool of characters
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"

    # 2. Pick characters using 'secrets'
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password
print("Generated secure password:", generate_secure_password())