import random
import string

def generate_password(length):
    # define the character sets to choose from
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # create a list of characters for the password
    password_chars = []
    password_chars.extend(random.choice(lowercase) for i in range(length // 4))
    password_chars.extend(random.choice(uppercase) for i in range(length // 4))
    password_chars.extend(random.choice(digits) for i in range(length // 4))
    password_chars.extend(random.choice(special_chars) for i in range(length // 4))

    # randomly choose additional characters until we reach the desired length
    while len(password_chars) < length:
        password_chars.append(random.choice(string.ascii_letters + string.digits + string.punctuation))

    # shuffle the characters and return the password as a string
    random.shuffle(password_chars)
    return ''.join(password_chars)

# prompt the user for the password length
length = int(input("Enter the length of the password: "))

# generate and print the password
password = generate_password(length)
print("Your password is:", password)
