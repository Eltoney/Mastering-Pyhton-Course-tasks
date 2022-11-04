def task1():
    my_list = [1, 5, 4, 3, 3, 2, 1]
    unique_list = [1, 5, 4, 3, 2]
    print(my_list)
    print(unique_list)
    print(type(unique_list))
    print(unique_list[:-1])


def task2():
    nums = {1, 2, 3}
    lets = {'A', 'B', 'C'}
    print(nums | lets)
    print(lets.union(nums))


def task3():
    my_set = {1, 2, 3}
    letters = {"A", "B", "C"}
    print(my_set)
    my_set.clear()
    print(my_set)

    my_set.add("A")
    my_set.add('B')

    print(my_set)
    my_set.discard("C")


def task4():
    set_one = {1, 2, 3}
    set_two = {1, 2, 3, 4, 5, 6}
    print(set_one.issubset(set_two))


if __name__ == "__main__":
    # task1()
    # task2()
    # task3()
    task4()