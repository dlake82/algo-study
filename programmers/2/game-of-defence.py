from heapq import heappush, heappop


def solution(n, k, enemy):
    if k == len(enemy):
        return k

    answer, now, h = 0, 0, []

    for i, e in enumerate(enemy):
        now += e
        heappush(h, -e)
        if n < now:
            if k == 0:
                return i
            k -= 1
            now += heappop(h)

    return answer


def solution(n, k, enemy):
    hq = []
    for round, monster in enumerate(enemy):
        heappush(hq, monster)
        if len(hq) > k:
            n -= heappop(hq)
        if n < 0:
            return round

    return len(enemy)


print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
