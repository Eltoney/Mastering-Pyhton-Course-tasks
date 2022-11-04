def get_score(**subjects):
    for sub, scor in subjects.items():
        print(f"{sub} => {scor}")


def task1():
    get_score(Math=90, Science=80, Language=70)
    get_score(Logic=70, Problems=60)


def get_people_scores(*name, **skills):
    if len(name) == 1:
        if len(skills) == 0:
            print(f"Hello {name[0]} You have no skills")
        else:
            print(f"Hello {name[0]}, This is your score table:")

    for skill, score in skills.items():
        print(f"{skill} => {score}")
    print('=' * 100)


def task2():
    get_people_scores("Osama", Math=90, Science=80, Language=70)
    get_people_scores("Mahmoud", Logic=70, Problems=60)
    get_people_scores(Logic=70, Problems=60)
    get_people_scores("Ahmed")


def task3():
    skills = {"python": "50", "c++": "80"}
    get_people_scores(**skills)
    get_people_scores("Ali")
    get_people_scores("Ali", **skills)


if __name__ == "__main__":
    # task1()
    # task2()
    task3()
