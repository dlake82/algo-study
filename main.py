"""
    소수
    - 소수 판별
    - 에라토스테네스의 체
"""

import random


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


"""
    최대공약수
    - 유클리드 호제법
"""


def gcd(a, b):
    while b > 1:
        a, b = b, a % b
    return a


print(gcd(123, 12))


"""
    기하
    - 직사각형에서 타일의 개수
    - 두 원의 관계
    - 벌집
"""


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
    a = n = 1
    if m == 1:
        return 1
    while a < m:
        a += 6 * (n - 1)
        n += 1

    return n - 1


print(house_of_bee(8))


"""
    자릿수의 합
    - 셀프 넘버
    - 특정 수의 개수
    - 각 자리수의 개수
"""


def sum_of_digits(n):
    return sum(list(map(int, [s for s in str(n)])))


def self_number(n):
    arr = [True] * (n + 1)
    for i in range(1, n + 1):
        idx = i + sum_of_digits(i)
        if idx < n + 1:
            arr[idx] = False
    return arr


arr = self_number(20)
for i, v in enumerate(arr):
    if v:
        print(i)


def surprise_n(n):
    answer = 0
    for i in range(1, n + 1):
        if i % sum_of_digits(i) == 0:
            answer += 1
    return answer


print(surprise_n(1000))


def count_digit(a, b, c):
    n = a * b * c
    arr = [0] * 10
    ds = [s for s in str(n)]
    for d in ds:
        arr[int(d)] += 1
    return arr


for i in count_digit(150, 266, 427):
    print(i)

"""
    정렬
    - 버블 정렬
    - 삽입 정렬
    - 버킷 정렬
    - 퀵 정렬
    - 병합 정렬
"""


def bubble_sort(arr):
    l = len(arr)
    for i in range(l - 1):
        for j in range(l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr = random.sample(range(1, 11), 10)
print(bubble_sort(arr))


def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break
    return arr


arr = random.sample(range(1, 11), 10)
print(insertion_sort(arr))


def bucket_sort(arr):
    bucket = [0] * (max(arr) + 1)
    for i in arr:
        bucket[i] += 1
    result = []
    for i in range(len(bucket)):
        if bucket[i] != 0:
            result.extend([i] * bucket[i])
    return result


arr = random.sample(range(1, 11), 10)
print(bucket_sort(arr))


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [i for i in arr if i < pivot]
    right = [i for i in arr if i > pivot]
    middle = [i for i in arr if i == pivot]

    return quick_sort(left) + middle + quick_sort(right)


arr = random.sample(range(1, 11), 10)
print(quick_sort(arr))


def merge_sort(arr):
    def merge(left, right):
        result = []
        l = r = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        if l < len(left):
            result.extend(left[l:])
        if r < len(right):
            result.extend(right[r:])
        return result

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


arr = random.sample(range(1, 11), 10)
print(merge_sort(arr))

"""
    탐색
    - 이진 탐색
    - 깊이 우선 탐색
    - 너비 우선 탐색
"""


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None


def binary_search_recursive(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, end)
    else:
        return binary_search_recursive(arr, target, start, mid - 1)


arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(arr, 7))
print(binary_search_recursive(arr, 7, 0, len(arr) - 1))

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "G", "H", "I"],
    "D": ["B", "E", "F"],
    "E": ["D"],
    "F": ["D"],
    "G": ["C"],
    "H": ["C"],
    "I": ["C", "J"],
    "J": ["I"],
}


def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])

    return visited


print(dfs(graph, "A"))

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "G", "H", "I"],
    "D": ["B", "E", "F"],
    "E": ["D"],
    "F": ["D"],
    "G": ["C"],
    "H": ["C"],
    "I": ["C", "J"],
    "J": ["I"],
}


def bfs(graph, start):
    visited = []
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])

    return visited


print(bfs(graph, "A"))


import heapq

"""
    최단 경로
    - 다익스트라 알고리즘
    - 플로이드 워셜 알고리즘
"""

graph = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances


print(dijkstra(graph, "A"))


n = 6
# this input is floyd_warshall algorithm's graph input
dist = [
    [0, 1, 2],
    [2, 5, 1],
    [3, 2, 4],
    [4, 1, 3],
    [2, 3, 1],
    [1, 5, 3],
    [4, 2, 2],
    [3, 4, 5],
]


graph = [[float("inf")] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    graph[i][i] = 0

for d in dist:
    a, b, c = d
    graph[a][b] = c
    graph[b][a] = c


def floyd_warshall(graph):
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph


print(floyd_warshall(graph))

"""
    그래프
    - 서로소 집합
    - 크루스칼 알고리즘
    - 위상 정렬
"""


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


graph = [
    (1, 7, 12),
    (1, 4, 28),
    (1, 2, 67),
    (1, 5, 17),
    (2, 4, 24),
    (2, 5, 62),
    (3, 5, 20),
    (3, 6, 37),
    (4, 7, 13),
    (5, 6, 45),
    (5, 7, 73),
]


def kruskal(v, graph):
    parent = [0] * (v + 1)
    edges = []
    result = 0

    for i in range(1, v + 1):
        parent[i] = i

    for edge in graph:
        a, b, cost = edge
        edges.append((cost, a, b))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            result += cost

    return result


print(kruskal(7, graph))

graph = {
    1: [2, 5],
    2: [3, 4],
    3: [4, 6],
    4: [6, 7],
    5: [6],
    6: [7],
}


def prim(graph):
    q, result, visited = [], 0, set()

    while q:
        cost, node = heapq.heappop(q)
        if node not in visited:
            visited.add(node)
            result += cost
            for i in graph[node]:
                heapq.heappush(q, i)
    return result


from collections import deque


def topology_sort(graph, indegree):
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    return result


n = 7
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

graph[1].append(2)
indegree[2] += 1
graph[1].append(5)
indegree[5] += 1
graph[2].append(3)
indegree[3] += 1
graph[3].append(4)
indegree[4] += 1
graph[4].append(6)
indegree[6] += 1
graph[5].append(6)
indegree[6] += 1
graph[6].append(7)
indegree[7] += 1

print(topology_sort(graph, indegree))
