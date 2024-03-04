from functools import reduce


def solution(elements):
    answer = 0
    n = len(elements)
    elements += elements[:-1]
    m = len(elements)
    dp = [[0] * (m) for _ in range(m)]
    for i in range(m):
        dp[i][i] = elements[i]

    for i in range(0, m):
        for j in range(i + 1, n if i < n else m - i):
            dp[i][j] = dp[i][j - 1] + dp[j][j]

    [print(arr) for arr in dp]
    test = set([1, 2]) | set([2, 3])
    sets = list(reduce(lambda acc, cur: set(acc) | set(cur), dp, []))
    print(sets)

    return answer


print(solution([7, 9, 1, 1, 4]))
