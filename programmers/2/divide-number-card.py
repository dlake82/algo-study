from math import sqrt
from collections import Counter
from functools import reduce


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

    answer = 0

    def get_factors_list(x): return list(
        map(Counter, map(get_factor, sorted(list(set(x))))))

    def get_sift(x): return reduce(lambda prev, next: {key: min(
        prev[key], next[key]) for key in prev if key in next}, x, x[0])

    a, b = get_sift(get_factors_list(arrayA)), get_sift(
        get_factors_list(arrayB))

    print(a, b)

    if not len(a) and not len(b):
        return 0

    if len(get_sift([a, b])):
        return 0

    return reduce(lambda acc, cur: acc * cur, a,
                  1) if len(a) else reduce(lambda acc, cur: acc * cur, b, 1)


print(solution([10, 17], [5, 20]))
