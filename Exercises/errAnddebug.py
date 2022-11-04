def task1():
    num = input("Add your number: ")

    if len(num) != 1:
        print("IndexError: Only One Character Allowed")
    elif not num.isnumeric():
        print("Exception: Only Numbers Allowed")
    elif int(num) == 0:
        print("ValueError: Number Must Be Larger Than 0")
    else:
        print(f"The number is {num}")


def task2():
    try:
        letter = input("Add Letter From A to Z")

    except len(letter) != 1:
        print("You Must Write One Character Only")
    else:
        print(f"Yor Typed {letter}")


def calculate(num1, num2) -> int:
    return num1 + num2


def task3():
    print(calculate(20, 30))


if __name__ == '__main__':
    # task1()
    task2()
    task3()
