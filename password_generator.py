import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    while True:
        try:
            length = int(input("\nEnter the length of the password (default is 12): "))
            if length <= 0:
                raise ValueError("Length must be a positive integer.")
            break
        except ValueError as ve:
            print("Invalid input:", ve)
    
    password = generate_password(length)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
