from math import sqrt
from collections import Counter
from functools import reduce
from itertools import combinations


def solution(arrayA, arrayB):
    def get_factor(n):
        d, result = 2, []
        while d <= int(sqrt(n)):
            if n % d != 0:
                d += 1
            else:
                result.append(d)
                n //= d
        if n > 1:
            result.append(n)
        return result

    ca, cb = [], []
    sa, sb = sorted(list(set(arrayA))), sorted(list(set(arrayB)))

    def get_factors_list(x): return list(
        map(Counter, map(get_factor, x)))

    def sift(prev, next):
        ret = {}
        for key in prev:
            if key in next:
                ret[key] = min(
                    prev[key], next[key])

        return ret

    def get_sift(x): return reduce(sift, x, x[0])

    fa, fb = get_factors_list(sa), get_factors_list(sb)

    a, b = get_sift(fa), get_sift(fb)

    if not len(a) and not len(b):
        return 0


print(solution([10, 20], [5, 17]))


def solution(elements):
    answer = 0
    elements += elements[:-1]
    n = len(elements)
    dp = [[0] * n for _ in range(n)]
    dp[0] = elements[:]
    for i in range(n):
        dp[i][0] = elements[i]

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + elements[i]

    print(dp)

    return answer
