from functools import reduce


def remove_chars(text):
    return text[1:len(text) - 1]


def task1():
    friends_map = ["AEmanS", "AAhmedS", "DSamehF", "LOsamaL"]
    cleaned_list = map(remove_chars, friends_map)
    cleaned_list = map(lambda text: text[1:-1], friends_map)
    for name in cleaned_list:
        print(name)


def task2():
    friends_filter = ["Osama", "Wessam", "Amal", "Essam", "Gamal", "Othman"]
    names = filter(lambda text: text[-1] == 'm', friends_filter)
    for name in names:
        print(name)


def task3():
    nums = [2, 4, 6, 2]
    tot = reduce(lambda x, y: x * y, nums)
    print(tot)


def task4():
    skills = ("HTML", "CSS", 10, "PHP", "Python", 20, "JavaScript")
    skills_enum = enumerate(reversed(skills) , 50)
    for indx, skill in skills_enum:
        if not str(skill).isnumeric():
            print(f"{indx} - {skill}")


if __name__ == "__main__":
    # task1()
    # task2()
    # task3()
    task4()
