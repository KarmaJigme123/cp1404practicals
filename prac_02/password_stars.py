"""
CP1404 - Practical 2
Student name: Karma Jigme Wangchuk
"""

SECRET = 5
def main():
    password = get_password(SECRET)
    print_asterisks(password)


def get_password(password_length):
    """Get password , ensuring it meets the least number of characters."""
    password = input(f"Enter password of at least {password_length} characters: ")
    while len(password) < password_length:
        print("Password too short")
        password = input(f"Enter password of at least {password_length} characters: ")
    return password


def print_asterisks(num):
    """Print asterisks corresponding to the password's length"""
    print('*' * len(num))


main()