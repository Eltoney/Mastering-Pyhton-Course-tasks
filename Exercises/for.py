def task1():
    my_nums = [15, 81, 5, 17, 20, 21, 13]
    my_nums.sort(reverse=True)
    cnt = 1
    for num in my_nums:
        if num % 5 == 0:
            print(f"{cnt} => {num}")
            cnt += 1
    else:
        print("All Numbers Printed")


def task2():
    for i in range(1, 21):
        if i in [6, 8, 10]:
            continue
        print(str(i).zfill(2))


def task3():
    my_ranks = {
        'Math': 'A',
        "Science": 'B',
        'Drawing': 'A',
        'Sports': 'C'
    }

    grades = {
        'A': 100,
        'B': 80,
        'C': 40
    }
    tot = 0
    for subject in my_ranks:
        print(f"My Rank in {subject} is {my_ranks[subject]} And this Equal {grades[my_ranks[subject]]} Points")
        tot += grades[my_ranks[subject]]
    else:
        print(f"Total score is {tot}")


def task4():
    students = {
        "Ahmed": {
            "Math": "A",
            "Science": "D",
            "Draw": "B",
            "Sports": "C",
            "Thinking": "A"
        },
        "Sayed": {
            "Math": "B",
            "Science": "B",
            "Draw": "B",
            "Sports": "D",
            "Thinking": "A"
        },
        "Mahmoud": {
            "Math": "D",
            "Science": "A",
            "Draw": "A",
            "Sports": "B",
            "Thinking": "B"
        }
    }
    grades = {
        'A': 100,
        'B': 80,
        'C': 40,
        'D': 20
    }
    for student in students:
        print('-' * 50)
        print(f"-- Student Name => {student}")
        print('-' * 50)
        tot = 0
        for subject, grade in students[student].items():
            print(f"- {subject} => {grades[grade]} Points")
            tot += grades[grade]
        print(f"Total Points For {student} is {tot}")


if __name__ == "__main__":
    # task1()
    # task2()
    # task3()
    task4()
