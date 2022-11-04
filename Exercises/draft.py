def remove_duplicate(word):
    if len(word) == 1:
        return word

    if word[0] == word[1]:
        return remove_duplicate(word[1:])
    return word[0] + remove_duplicate(word[1:])


def check_parity():
    my_list = [2, 4, 6]
    print(my_list)
    print(all(my_list))
    if all(my_list) % 2 == 0:
        print("All numbers are even")
    else:
        print("Some numbers are odd")


def test_id():
    a = 2
    b = a
    print(id(a))
    print(id(b))
    b = 3
    print(a, b)
    print(id(a))
    print(id(b))


def format_text(text):
    return f"The word is: {text}"


def map_test():
    my_list = ['ali', 'nader', 'hos']
    # names = map(format_text, my_list)
    names = map(lambda text: f"Haha {text}", my_list)
    for name in names:
        print(name)


if __name__ == "__main__":
    map_test()

    # test_id()

    # check_parity()

    # print(remove_duplicate("wwwwooooorrlllddd"))
    # print(remove_duplicate("abbbbbbcccccccccccccccc"))
    # print(remove_duplicate("abcdvfvgbgnbgibngkbnkjgfbjbfjs"))
    # print(remove_duplicate("abccvfvvbnfnfnbjgnbkjgnbj"))
    # print(remove_duplicate("abvgbgnkjbngnbc"))
