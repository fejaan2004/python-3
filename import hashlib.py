import hashlib

# Initialize an empty password vault dictionary
password_vault = {}

# Function to add a new password to the vault
def add_password(website, password):
    # Hash the password before storing it (for added security)
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_vault[website] = hashed_password
    print(f"Password for {website} added successfully!")

# Function to retrieve a password from the vault
def get_password(website):
    if website in password_vault:
        return password_vault[website]
    else:
        return None

# Function to list all websites and their passwords
def list_passwords():
    print("Website Passwords:")
    for website, password in password_vault.items():
        print(f"{website}: {password}")

# Main program loop
while True:
    print("\nPassword Vault Menu:")
    print("1. Add Password")
    print("2. Retrieve Password")
    print("3. List Passwords")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        website = input("Enter website name: ")
        password = input("Enter password: ")
        add_password(website, password)
    elif choice == "2":
        website = input("Enter website name: ")
        stored_password = get_password(website)
        if stored_password:
            print(f"Password for {website}: {stored_password}")
        else:
            print(f"No password found for {website}")
    elif choice == "3":
        list_passwords()
    elif choice == "4":
        print("Exiting Password Vault. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
