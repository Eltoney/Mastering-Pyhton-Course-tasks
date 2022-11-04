def task1():
    import random
    rnd = random.randint(10, 50)
    rnd_even = random.randrange(2, 11, 2)
    rnd_odd = random.randrange(1, 10, 2)
    print(f"Random Number Between 10 And 50 => {rnd}")
    print(f"Random Even Number Between 2 And 10 => {rnd_even}")
    print(f"Random Odd Number Between 1 And 9 => {rnd_odd}")


def task2():
    import my_mod
    print(my_mod.say_hello("Ali"))
    print(my_mod.say_welcome("Ali"))


def task3():
    from my_mod import say_welcome
    print(say_welcome("Nada"))


def task4():
    from my_mod import say_welcome as new_welcome
    print(new_welcome("Heba"))


if __name__ == '__main__':
    # task1()
    # task2()
    # task3()
    task4()
