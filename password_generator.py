import random
import string

letters = string.ascii_letters
numbers = string.digits
signs = string.punctuation


def password_generator(length: int, *args):
    password = []
    combo = ''.join(args)
    for i in range(length):
        password.append(random.choice(combo))

    return "".join(password)
