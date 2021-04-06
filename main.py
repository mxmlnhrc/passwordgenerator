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


def congrats(pw):
    print("****************************")
    print("This is your new password")
    print(pw)
    print("****************************")


def generate_password(password_lenght):
    global password
    for i in range(password_lenght):
        random.shuffle(poll)
        password += secrets.choice(poll)

    return password


while True:
    password = ""
    print("Welcome, Create a new password")
    try:
        password_lenght = int(
            input("How long should the password be?\nLeave blank(12)\n>>> "))
        if password_lenght == '':
            password_lenght = 12

    except ValueError:
        pass

    password = generate_password(password_lenght)

    print(password)

    print(f"Do you want to get {password}?")
    print("[y/N]")

    user_in = input(">>> ")

    if user_in.lower() == 'q':
        break
    elif user_in.lower() == "y":
        congrats(password)
    elif user_in.lower() == "n":
        continue
    else:
        print("We couldn't find this comand!")
        user_in = input("Press any key to continue")