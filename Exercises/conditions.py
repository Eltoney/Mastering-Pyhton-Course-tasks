def task1():
    num1 = int(input("Enter first  Number: "))
    num2 = int(input("Enter second Number:"))
    operation = input("Enter one of the following operations (+,-, /, *)").strip()
    if operation == '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"{num1} + {num2} = {num1 * num2}")
    elif operation == '*':
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Wrong operation")


def task2():
    age = 15
    print("Age Is suitalbe for you") if age > 16 else print("young")


def task3():
    age = int(input("Enter your age: "))
    if age in range(10, 101):
        months = age * 12
        weeks = months * 4
        days = weeks * 7
        hours = days * 24
        minutes = hours * 60
        seconds = minutes * 60
        print(f"age in months is {months:,}")
        print(f"age in weeks is {weeks:,}")
        print(f"age in days is {days:,}")
        print(f"age in hours is {hours:,}")
        print(f"age in minutes is {minutes:,}")
        print(f"age in seconds is {seconds:,}")

    else:
        print("Not valid age")


def task4():
    country = input("Input Your Country").strip().capitalize()
    countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
    price = 100
    discount = 30
    if country in countries:
        print(f"There is a discount for {country} and the course price is {price - discount}")
    else:
        print(f"The course price is {price}")


if __name__ == "__main__":
    # task1()
    # task2()
    # task3()
    task4()
