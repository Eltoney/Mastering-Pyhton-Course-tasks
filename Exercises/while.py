def task1():
    num = int(input("Enter a number bigger than zero: "))
    cnt = 0
    if num <= 0:
        print(f"{num} is invalid input")
    else:
        num -= 1
        while num > 0:
            if num != 6:
                cnt += 1
                print(num)
            num -= 1
        else:
            print(f"Iteration done, {cnt} numbers is printed")


def task2():
    friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
    idx = 0
    cnt = 0
    while idx < len(friends):
        if friends[idx][0].isupper():
            print(friends[idx])
        else:
            cnt += 1
        idx += 1
    else:
        print(f"Friends is printed and {cnt} is ignored")


def task3():
    skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

    while skills:
        print('\n'.join(skills))

        break


def task4():
    my_friends = []
    max_friends = 4

    while max_friends > 0:
        name = input().strip()
        if name.isupper():
            print(f"{name} is not a valid name")
        else:
            my_friends.append(name.capitalize())
            print(f"{name} capitalized and add to the list")
            max_friends -= 1
        print(f"{max_friends} friends remain")


if __name__ == "__main__":
    # task1()
    # task2()
    task3()
    task4()
