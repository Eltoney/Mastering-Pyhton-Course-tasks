def convert_base(sub, b, k):
    ans = []
    while sub > 0:
        ans.append(str(sub % b))
        sub //= b

    while len(ans) < k:
        ans.append('0')
    return ''.join(reversed(ans))


def preform_sub(n, b, k):
    n = ''.join(sorted(list(n)))
    small = int(n, b)
    big = int(''.join(reversed(list(n))), b)
    return convert_base(big - small, b, k)


def solution(n, b):
    cnt = 0
    k = len(n)
    d = dict()
    while cnt < 20:
        d[n] = cnt
        cnt += 1
        n = preform_sub(n, b, k)
        if n in d.keys():
            return cnt - d[n]

    return cnt


if __name__ == '__main__':
    n = '0'
    b = 10
    print(solution(n, b))
