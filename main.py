def _sum(n):
    return n + (n + 1) // 2


n = 10
print(_sum(n))


def _max(arr):
    MAX = 0
    for i in arr:
        if i > MAX:
            MAX = i
    return MAX


arr = [1, 2, 3, 4, 5]
print(_max(arr))


def _min(arr):
    MIN = float("inf")
    for i in arr:
        if i < MIN:
            MIN = i
    return MIN


print(_min(arr))


def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % 2 == 0:
            return False
    return True


for i in range(2, 20):
    if is_prime(i):
        print(i, end=" ")
print()


def erathosthenes(n):
    factor = [True] * (n + 1)
    factor[0] = factor[1] = False

    for i in range(2, int(n**0.5) + 1):
        if factor[i]:
            for j in range(i * 2, n + 1, i):
                factor[j] = False

    return factor


print(erathosthenes(20))


def gcd(a, b):
    while b > 1:
        a, b = b, a % b
    return a


print(gcd(123, 12))


def sum_of_three_bar(a, b, c):
    if a + b > c:
        c = a + b - 1
    return a + b + c


ret = sum_of_three_bar(1, 2, 5)
print(ret)


def turret(coord):
    x1, y1, r1, x2, y2, r2 = coord

    dist = (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5
    diff = abs(r1 - r2)
    s = r1 + r2

    # 원이 같을 때
    if dist == diff == 0:
        return -1
    # 원이 외접하거나 내접할 때
    if dist == s or dist == diff:
        return 1
    # 원이 두 점에서 만날 때
    if diff < dist < s:
        return 2
    return 0


print(turret([1, 1, 1, 1, 1, 5]))


def house_of_bee(m):
    a = 1
    n = 1
    if m == 1:
        return 1
    while a < m:
        a += 6 * (n - 1)
        n += 1

    return n - 1


print(house_of_bee(8))
