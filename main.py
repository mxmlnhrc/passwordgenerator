import random
import secrets

password_lenght = 12

small_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

upper_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symbols = [
    '<', '>', ',', ';', '.', ':', '-', '_', '#', "'", '+', '*', '~', '`', '´',
    '?', "=", '}', ']', ')', '[', '(', '{', '/', '&', '%', '$', '§', '!', '°',
    '^', '"'
]

poll = small_letters + upper_letters + numbers + symbols

password = ""


def generate_password(password_lenght):
    global password
    for i in range(password_lenght):
        random.shuffle(poll)
        password += secrets.choice(poll)

    return password


password = generate_password(password_lenght)
print(password)