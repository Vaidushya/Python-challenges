#-- Homework --#

import random
import string

def generate_password(length=12):
    chars = string.ascii_letters + string.digits
    password = random.sample(chars, length)
    random.shuffle(password)
    return ''.join(password)

print("Generated password:", generate_password())