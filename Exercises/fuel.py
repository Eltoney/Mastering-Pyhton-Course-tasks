def valid(i, j, n, m):
    return 0 <= i < n and 0 <= j < m


def solution(mat):
    n, m = len(mat), len(mat[0])
    dis = dict()
    path = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    path_id = 0
    dis[(0, 0, 0)] = 1
    path.append((0, 0, 0))

    while path_id < len(path):
        cur = path[path_id]
        path_id += 1

        if cur[0] == n - 1 and cur[1] == m - 1:
            return dis[cur]

        for k in range(4):
            nx = cur[0] + dx[k]
            ny = cur[1] + dy[k]

            if valid(nx, ny, n, m):
                new = (nx, ny, cur[2] + int(mat[nx][ny] == 1))
                if new not in dis and new[2] < 2:
                    dis[new] = dis[cur] + 1
                    path.append(new)


if __name__ == '__main__':
    print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
    print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1],
                    [0, 0, 0, 0, 0, 0]]))
