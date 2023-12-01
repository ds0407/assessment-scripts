# Fix this loop so that it runs and if the user enters their credentials incorrectly 3 times, they receive an access denied message.
# If they enter the correct details they receive an access granted message and the terminal program exits.

def main():
    login_attempts = 0
    max_attempts = 3

    username = "admin"
    password = "cisco123"

    while login_attempts < max_attempts:
        name_input = int(input("Enter your username: "))
        password_input = int(input("Enter your password: "))

        if name_input == username and password_input == password:
            print("\nAccess granted")
        else:
            login_attempts += 1
            print("\nIncorrect Credentials. Please try again.")
            
    if login_attempts == max_attempts:
        print("\nAccess denied.\n")

if "__name__" == "__main__":
    main()