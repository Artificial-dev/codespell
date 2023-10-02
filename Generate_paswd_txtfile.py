import itertools

def generate_passwords(length, characters, num_passwords):
    passwords = []

    for _ in range(num_passwords):
        password = ''.join(random.choice(characters) for _ in range(length))
        passwords.append(password)

    return passwords

def filter_passwords(passwords, filter_condition):
    return [password for password in passwords if filter_condition(password)]

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special(password):
    special_chars = "!@#$%^&*()_+{}:;<>,.?"
    return any(char in special_chars for char in password)

if __name__ == "__main__":
    import random

    length = int(input("Enter the length of the passwords: "))
    num_passwords = int(input("Enter the number of passwords to generate: "))

    characters = string.ascii_letters + string.digits + string.punctuation

    passwords = generate_passwords(length, characters, num_passwords)

    filter_criteria = [
        ("Lowercase", has_lowercase),
        ("Uppercase", has_uppercase),
        ("Digit", has_digit),
        ("Special Character", has_special)
    ]

    for filter_name, filter_condition in filter_criteria:
        filtered_passwords = filter_passwords(passwords, filter_condition)
        print(f"\nPasswords with {filter_name}:")
        print(filtered_passwords)
