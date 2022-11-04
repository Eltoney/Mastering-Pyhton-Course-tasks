def product(lst):
    ans = 1
    for x in lst:
        ans *= x
    return ans


def solution(xs):
    pos, neg = [], []
    for x in xs:
        if x < 0:
            neg.append(x)
        elif x > 0:
            pos.append(x)

    pos_prod = product(pos)
    neg_prod = 1

    neg.sort()

    if len(neg) % 2 == 1:
        neg_prod = product(neg[:-1])
    else:
        neg_prod = product(neg)

    ans = 0
    if len(pos) == 0 and len(neg) == 0:
        ans = 0
    elif len(pos) == 0 and len(neg) == 1:
        ans = neg[0]
    else:
        ans = pos_prod * neg_prod

    ans = str(ans)
    return ans


if __name__ == '__main__':
    e = [-5 , 0 , 0]
    print(solution(e))

    a = [2, 0, 2, 0, 2]
    print(solution(a))

    print(solution([-2, -3, 4, -5]))

    print(solution([9]))
    print(solution([0]))
