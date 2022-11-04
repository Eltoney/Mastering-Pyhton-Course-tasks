def task1():
    values = (0, 1, 2)

    if any(values):
        my_var = 0

    my_list = [True, 1, 1, ["A", "B"], 10.5, my_var]

    if all(my_list[:4]) or all(my_list[:6]) or all(my_list[:]):

        print("Good")

    else:

        print("Bad")


def task2():
    v = 40

    my_range = list(range(v))

    print(sum(my_range, v) + pow(v, v, v))


def task3():
    n = 20

    l = list(range(n))

    if round(sum(l) / n) == max(0, 3, 10, 2, -100, -23, 9):
        print("Good")

    # Output => Good


def my_all(my_list):
    for x in my_list:
        if not bool(x):
            return False
    return True


def my_any(my_list):
    for x in my_list:
        if bool(x):
            return True
    return False


def my_min(my_list):
    mn = my_list[0]
    for x in my_list:
        if x < mn:
            mn = x
    return mn


def my_max(my_list):
    mx = my_list[0]
    for x in my_list:
        if x > mx:
            mx = x
    return mx


def task4():
    print(my_all([1, 2, 3]))  # True
    print(my_all([1, 2, 3, []]))  # False

    # my_any
    print(my_any([0, 1, [], False]))  # True
    print(my_any([(), 0, False]))  # False

    # my_min
    print(my_min([10, 100, -20, -100, 50]))  # -100
    print(my_min((10, 100, -20, -100, 50)))  # -100

    # my_max
    print(my_max([10, 100, -20, -100, 50, 700]))  # 700
    print(my_max((10, 100, -20, -100, 50, 700)))


if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    task4()
