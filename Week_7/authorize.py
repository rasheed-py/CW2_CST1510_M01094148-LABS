import bcrypt

USER_DATA_FILE = "DATA/users.txt"

def hash_password(plain_text_pass):
    pass_bytes = plain_text_pass.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pass = bcrypt.hashpw(pass_bytes, salt)

    return hashed_pass

def verify_password(plain_text_pass, hashed_pass):
    return bcrypt.checkpw(
        plain_text_pass.encode('utf-8'),
        hashed_pass if isinstance(hashed_pass, bytes) else hashed_pass.encode('utf-8')
    )


def register_user(user_name, password):
    open(USER_DATA_FILE, 'a').close()
    with open(USER_DATA_FILE, 'r+') as file:
        for line in file:
            if line.startswith(f"{user_name},"):
                print(f"Error: Username '{user_name}' already exists.")
                return False

        # Hash password and add new user
        hashed = hash_password(password).decode('utf-8')
        file.write(f"{user_name},{hashed}\n")

    print(f"Success: User '{user_name}' registered successfully!")
    return True

def user_exists(user_name):
    open(USER_DATA_FILE, 'a').close()
    with open(USER_DATA_FILE, 'r') as file:
        for line in file:
             if line.startswith(f"{user_name},"):
                 return True

    return False

def login_user(user_name, password):
    with open(USER_DATA_FILE, 'r') as file:
        for line in file:
            stored_username, stored_hashed = line.strip().split(',', 1)

            if stored_username == user_name:
                if verify_password(password, stored_hashed.encode('utf-8')):
                    print(f"Success: Welcome, '{user_name}'")
                    return True
                else:
                    print("Error:Invalid password")
                    return False

    print("Error: Username not found")
    return False

def validate_username(user_name):
    if user_name.isalnum() and 3 <= len(user_name) <= 20:
        return True, ""
    return False, "Username must be 3–20 letters/numbers only."

def validate_password(password):
    if len(password) < 6:
        return False, "Password too short (min 6)."
    if not any(c.isupper() for c in password):
        return False, "Need at least one uppercase letter."
    if not any(c.islower() for c in password):
        return False, "Need at least one lowercase letter."
    if not any(c.isdigit() for c in password):
        return False, "Need at least one number."
    return True, ""


def display_menu():
    print("\n" + "=" * 50)
    print("  SECURE AUTHENTICATION SYSTEM")
    print("=" * 50)
    print("[1] Register a new user")
    print("[2] Login")
    print("[3] Exit")
    print("-" * 50)

def main():
    print("\nWelcome to the Authentication System!")

    while True:
        display_menu()
        choice = input("Select an option (1–3): ").strip()

        if choice == '1':
            print("\n--- USER REGISTRATION ---")
            user_name = input("Enter username: ").strip()
            valid, msg = validate_username(user_name)
            if not valid:
                print(f"Error: {msg}")
                continue

            password = input("Enter password: ").strip()
            valid, msg = validate_password(password)
            if not valid:
                print(f"Error: {msg}")
                continue

            confirm = input("Confirm password: ").strip()
            if password != confirm:
                print("Error: Passwords do not match.")
                continue

            register_user(user_name, password)

        elif choice == '2':
            print("\n--- USER LOGIN ---")
            user_name = input("Enter username: ").strip()
            password = input("Enter password: ").strip()
            login_user(user_name, password)

        elif choice == '3':
            print("\nExiting... Goodbye!")
            break

        else:
            print("Error: Invalid option. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()