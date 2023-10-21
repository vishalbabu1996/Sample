import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    if num_passwords <= 0 or password_length <= 0:
        print("Please enter valid numbers for the number and length of passwords.")
        return

    passwords = [generate_password(password_length) for _ in range(num_passwords)]

    for i, password in enumerate(passwords):
        print(f"Password {i+1}: {password}")

if __name__ == "__main":
    main()