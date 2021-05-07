from string import ascii_letters, digits
import random

char = ascii_letters + digits

# fake password generator
def generate():
    fake_password = (random.choices(char, k=16))

    for p in '!$=@?.':
        fake_password.insert(random.randint(0, len(fake_password)), p)

    fake_password = "".join(fake_password)

    return fake_password
