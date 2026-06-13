import os
from datetime import datetime
import getpass
from cryptography.fernet import Fernet

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

KEY_FILE = os.path.join(BASE_DIR, "secret.key")
ENTRIES_DIR = os.path.join(BASE_DIR, "entries")

def generate_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as key_file:
            key_file.write(key)


def load_key():
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def encrypt_text(text):
    key = load_key()
    cipher = Fernet(key)
    return cipher.encrypt(text.encode())


def decrypt_text(encrypted_text):
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_text).decode()


def create_entry():
    title = input("Enter the title of your diary entry: ")
    content = input("Write your diary entry: ")

    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    encrypted_content = encrypt_text(content)

    os.makedirs(ENTRIES_DIR, exist_ok=True)

    # Remove invalid Windows filename characters
    safe_title = "".join(
        c for c in title if c not in r'\/:*?"<>|'
    )

    file_name = f"{date}_{safe_title}.txt"

    with open(os.path.join(ENTRIES_DIR, file_name), "wb") as file:
        file.write(encrypted_content)

    print(f"Diary entry '{title}' saved successfully!")


def list_entries():
    os.makedirs(ENTRIES_DIR, exist_ok=True)

    entries = os.listdir(ENTRIES_DIR)

    if not entries:
        print("No diary entries found.")
        return

    print("\nYour Diary Entries:")
    for index, entry in enumerate(entries, start=1):
        print(f"{index}. {entry}")


def read_entry():
    os.makedirs(ENTRIES_DIR, exist_ok=True)

    entries = os.listdir(ENTRIES_DIR)

    if not entries:
        print("No diary entries found.")
        return

    print("\nAvailable Entries:")
    for index, entry in enumerate(entries, start=1):
        print(f"{index}. {entry}")

    file_name = input("\nEnter the exact file name: ")

    file_path = os.path.join(ENTRIES_DIR, file_name)

    try:
        with open(file_path, "rb") as file:
            encrypted_content = file.read()

        content = decrypt_text(encrypted_content)

        print("\n" + "=" * 40)
        print(f"Diary Entry: {file_name}")
        print("=" * 40)
        print(content)

    except FileNotFoundError:
        print("Entry not found.")


def authenticate():
    password = getpass.getpass("Enter your diary password: ")

    if password == "mypassword":  # Demo password
        print("Authentication successful!")
        return True

    print("Authentication failed. Access denied.")
    return False


def main():
    generate_key()

    if authenticate():
        while True:
            print("\n1. Create a new diary entry")
            print("2. List all diary entries")
            print("3. Read a diary entry")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                create_entry()

            elif choice == "2":
                list_entries()

            elif choice == "3":
                read_entry()

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()