from operations import *
from history import save_history


def menu():
    print("\n========== CS50 Calculator ==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Power")
    print("7. Exit")


while True:

    menu()

    choice = input("\nChoose: ")

    if choice == "7":
        print("Thanks for using the calculator.")
        break

    if choice not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid option.")
        continue

    try:
        a = float(input("First number: "))
        b = float(input("Second number: "))
    except ValueError:
        print("Numbers only.")
        continue

    if choice == "1":
        operator = "+"
        result = add(a, b)

    elif choice == "2":
        operator = "-"
        result = subtract(a, b)

    elif choice == "3":
        operator = "*"
        result = multiply(a, b)

    elif choice == "4":
        operator = "/"
        result = divide(a, b)

    elif choice == "5":
        operator = "%"
        result = modulus(a, b)

    elif choice == "6":
        operator = "**"
        result = power(a, b)

    print(f"\nResult = {result}")

    save_history(a, operator, b, result)
