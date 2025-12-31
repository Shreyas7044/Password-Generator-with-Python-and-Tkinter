import random
import string
import tkinter as tk
from tkinter import messagebox

# ---------------- CLI Password Generator ---------------- #
def cli_password_generator():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be greater than 0")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        print("\nGenerated Password:")
        print(password)
    except:
        print("Please enter a valid number")


# ---------------- GUI Password Generator ---------------- #
def generate_password():
    password = []
    for i in range(5):
        alpha = random.choice(string.ascii_letters)
        symbol = random.choice(string.punctuation)
        number = random.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(number)

    final_password = "".join(password)
    label.config(text=final_password)


def launch_gui():
    global label
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x250")

    title = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"))
    title.pack(pady=10)

    button = tk.Button(root, text="Generate Password", font=("Arial", 12), command=generate_password)
    button.pack(pady=10)

    label = tk.Label(root, font=("Arial", 14, "bold"))
    label.pack(pady=10)

    root.mainloop()


# ---------------- Main ---------------- #
if __name__ == "__main__":
    print("Choose Mode:")
    print("1. CLI Password Generator")
    print("2. GUI Password Generator")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        cli_password_generator()
    elif choice == "2":
        launch_gui()
    else:
        print("Invalid choice"