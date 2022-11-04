def task1():
    print(True)
    print(bool(1))
    print(bool({2}))
    print(bool("a"))
    print(False)
    print(bool(0))
    print(bool({}))
    print(bool(""))


def task2():
    cplus = 70
    csharp = 55
    python = 55
    print(cplus > 50 and csharp > 50 and python > 50)


def task3():
    num_one = 10
    num_two = 20
    num = 20
    print(bool((num > num_one) ^ (num > num_two)))
    print(num > num_one and num > num_two)


def task4():
    num_one = 10
    num_two = 20
    result = num_one + num_two
    print(result)
    result **= 3
    print(result)
    result = result % 26000
    print(result)
    result /= 5
    print(result)
    result = str(result)
    print(type(result))


if __name__ == "__main__":
    # task1()
    # task2()
    # task3()
    task4()
