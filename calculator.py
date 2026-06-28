from datetime import datetime


def save_history(operation, result):
    """Save operations to history.txt"""
    with open("history.txt", "a") as file:
        file.write(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] "
            f"{operation} = {result}\n"
        )


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero."
    return x / y


def power(x, y):
    return x ** y


def modulus(x, y):
    return x % y


def square_root(x):
    if x < 0:
        return "Error: Negative number."
    return x ** 0.5


def clear_history():
    open("history.txt", "w").close()
    print("History cleared successfully.")


def show_history():
    try:
        with open("history.txt", "r") as file:
            content = file.read()

            if content:
                print("\n===== History =====")
                print(content)
            else:
                print("History is empty.")

    except FileNotFoundError:
        print("No history found.")


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def main():

    print("=" * 45)
    print("        CS50 Python Calculator")
    print("=" * 45)

    while True:

        print("""
1) Addition
2) Subtraction
3) Multiplication
4) Division
5) Power
6) Modulus
7) Square Root
8) Show History
9) Clear History
0) Exit
""")

        choice = input("Select an option: ")

        if choice == "0":
            print("Goodbye!")
            break

        elif choice == "8":
            show_history()
            continue

        elif choice == "9":
            clear_history()
            continue

        elif choice == "7":
            num = get_number("Enter number: ")
            result = square_root(num)
            print("Result:", result)

            if not isinstance(result, str):
                save_history(f"sqrt({num})", result)

            continue

        elif choice in ["1", "2", "3", "4", "5", "6"]:

            num1 = get_number("First number: ")
            num2 = get_number("Second number: ")

            if choice == "1":
                result = add(num1, num2)
                operation = f"{num1} + {num2}"

            elif choice == "2":
                result = subtract(num1, num2)
                operation = f"{num1} - {num2}"

            elif choice == "3":
                result = multiply(num1, num2)
                operation = f"{num1} * {num2}"

            elif choice == "4":
                result = divide(num1, num2)
                operation = f"{num1} / {num2}"

            elif choice == "5":
                result = power(num1, num2)
                operation = f"{num1} ^ {num2}"

            elif choice == "6":
                result = modulus(num1, num2)
                operation = f"{num1} % {num2}"

            print("Result:", result)

            if not isinstance(result, str):
                save_history(operation, result)

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
