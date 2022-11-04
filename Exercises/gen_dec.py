def reverse_string(my_string):
    for i in range(len(my_string) - 1, -1, -1):
        yield my_string[i]


def task1():
    for c in reverse_string("Elzero"):
        print(c)
        print("#######")


def my_dec(func):
    def wrapper():
        print("Sugar added from Dec")
        func()
        print("#" * 50)

    return wrapper


@my_dec
def make_tea():
    print("Tea Created")


@my_dec
def make_coffe():
    print("Coffe Created")


def task2():
    make_tea()
    make_coffe()


if __name__ == '__main__':
    # task1()
    task2()
