from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def solution(board):
    def bfs(a, b):
        nonlocal flag
        d, minn, visited = deque([[a, b, 0]]), float("inf"), []

        while d:
            x, y, c = d.popleft()
            for i in range(4):
                xx, yy = x, y
                while (0 <= xx < n and 0 <= yy < m) and arr[xx][yy] != "D":
                    xx, yy = xx + dx[i], yy + dy[i]
                xx, yy = xx - dx[i], yy - dy[i]
                if [x, y, xx, yy] in visited:
                    continue
                if arr[xx][yy] == "G" and c < minn:
                    flag, minn = True, c + 1
                visited.append([x, y, xx, yy])
                d.append([xx, yy, c + 1])

        return minn

    arr = [list(i) for i in board]
    n, m, flag = len(arr), len(arr[0]), False

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'R':
                result = bfs(i, j)
                return result if flag else -1


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
