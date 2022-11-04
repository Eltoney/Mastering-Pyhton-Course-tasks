def task1():
    name = input("Enter you Name: ").strip().capitalize()
    print(f"Hello {name}, Happy to see you!")


def task2():
    age = int(input("Enter your age: "))
    if age < 16:
        print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
    else:
        print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")


def task3():
    fname = input("Enter your first name: ").strip().capitalize()
    lname = input("Enter your last  name: ").strip().capitalize()
    print(f"Hello {fname} {lname:.1s}")


def task4():
    email = input("Enter your Email: ").strip().lower()
    print(f"Your Name is: {email[:email.index('@')].capitalize()}")
    print(f"Email service provider is: {email[email.index('@') + 1: email.index('.')]}")
    print(f"Top Level domain: {email[email.index('.') + 1:]}")


if __name__ == "__main__":
    # task1()
    # task2()
    # task3()
    task4()
