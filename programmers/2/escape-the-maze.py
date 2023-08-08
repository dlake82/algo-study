from collections import deque


def solution(maps):
    def bfs(i, j, target):
        d = deque([[i, j, 0]])
        visited = [[False] * m for _ in range(n)]
        visited[i][j] = True

        while d:
            ox, oy, k = d.popleft()

            for i in range(4):
                x, y = ox + dx[i], oy + dy[i]

                if 0 <= x < n and 0 <= y < m and not visited[x][y]:
                    visited[x][y] = True
                    if arr[x][y] == 'X':
                        continue
                    if arr[x][y] == target:
                        return k + 1
                    d.append([x, y, k + 1])

        return -1

    dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

    arr = [list(r) for r in maps]
    n, m = len(arr), len(arr[0])
    sx, sy, lx, ly, L, S = [0] * 6

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 'S':
                sx, sy = i, j
            if arr[i][j] == 'L':
                lx, ly = i, j

    L = bfs(sx, sy, 'L')
    if L == -1:
        return -1
    S = bfs(lx, ly, 'E')
    if S == -1:
        return -1

    return L + S


print(solution(["LOOXS", "OOOOX", "OOOOO", "OOOOO", "EOOOO"]))
