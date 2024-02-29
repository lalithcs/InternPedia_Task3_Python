import secrets
import string
import pyperclip

# Function to generate a secure random password
def generate_password(length, complexity):
    # Define character sets based on complexity
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Initialize password characters with lowercase letters
    password_chars = list(lowercase_letters)

    # Add characters based on complexity requirements
    if 'uppercase' in complexity:
        password_chars.extend(uppercase_letters)
    if 'digits' in complexity:
        password_chars.extend(digits)
    if 'symbols' in complexity:
        password_chars.extend(symbols)

    # Generate password using secure random choice
    password = ''.join(secrets.choice(password_chars) for _ in range(length))
    return password

# Function to display passwords and copy to clipboard
def display_passwords(passwords):
    print("Generated Passwords:")
    for password in passwords:
        print(password)
    print()

    copy_to_clipboard = input("Do you want to copy a password to clipboard? (yes/no): ").lower()
    if copy_to_clipboard == 'yes':
        try:
            index = int(input("Enter the index of the password you want to copy: "))
            if 0 <= index < len(passwords):
                pyperclip.copy(passwords[index])
                print("Password copied to clipboard successfully!")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid index. Please enter a number.")

# Main function
def main():
    print("Welcome to the Random Password Generator!")

    while True:
        try:
            length = int(input("Enter password length: "))
            if length <= 0:
                print("Password length must be a positive integer.")
                continue

            complexity = input("Enter password complexity (uppercase, lowercase, digits, symbols separated by commas): ").lower().split(',')
            passwords_count = int(input("Enter the number of passwords to generate: "))

            passwords = [generate_password(length, complexity) for _ in range(passwords_count)]
            display_passwords(passwords)

            another_generation = input("Do you want to generate more passwords? (yes/no): ").lower()
            if another_generation != 'yes':
                print("Thank you for using the Random Password Generator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter valid integers.")

if __name__ == "__main__":
    main()
