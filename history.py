from datetime import datetime


def save_history(a, operator, b, result):

    with open("history.txt", "a") as file:

        file.write(
            f"{datetime.now()} : {a} {operator} {b} = {result}\n"
        )
