def calculate(num1, num2, opr='a'):
    opr = opr.lower()
    if opr in ['a', '+', 'add']:
        return num1 + num2
    elif opr in ['s', '-', 'subtract']:
        return num1 - num2
    elif opr in ['m', '+', 'multiply']:
        return num1 * num2
    elif opr in ['d', '/', 'divide']:
        if num2 == 0:
            print("Error divide by zero")
        else:
            return num1 / num2
    else:
        print(f"{opr} is not a valid option")


def addition(*nums):
    tot = 0
    for num in nums:
        if num == 10:
            continue
        elif num == 5:
            tot -= 5
        else:
            tot += num
    return tot


def show_skills(name, *skills):
    if len(skills) == 0:
        print(f"Hi {name}, you need to work harder to gain some skills")
    else:
        print(f"Hi {name}, here is your skills list:")
        for skill in skills:
            print(f"- {skill}")


def say_hello(name="Unknown", age="Unknown", country="Unknown"):
    return f"Hello {name} , Your are from {country} and your age is {age}"


if __name__ == "__main__":
    # print(calculate(10, 20))  # 30
    # print(calculate(10, 20, "AdD"))  # 30
    # print(calculate(10, 20, "a"))  # 30
    # print(calculate(10, 20, "A"))  # 30
    #
    # print(calculate(10, 20, "S"))  # -10
    # print(calculate(10, 20, "subTRACT"))  # -10
    #
    # print(calculate(10, 20, "Multiply"))  # 200
    # print(calculate(10, 20, "m"))

    # print(addition(10, 20, 30, 10, 15))  # 65
    # print(addition(10, 20, 30, 10, 15, 5, 100))  # 160

    # show_skills("Osama", "HTML", "CSS", "JS", "Python")
    # show_skills("Nader", "HTML", "CSS")
    # show_skills("Noha")

    print(say_hello("Nada"))
    print(say_hello("Noha", 35, "USA"))
    print(say_hello())
