from collections import defaultdict


def solution(book_time):
    def get_time(time):
        HH, MM = map(int, time.split(":"))
        # 청소 시간 보정
        return HH * 60 + MM

    MAX, now = 0, 0

    books = defaultdict(int)

    for b in book_time:
        s, e = get_time(b[0]), get_time(b[1])
        books[s] += 1
        books[e + 10] -= 1

    books = sorted(list(map(list, books.items())))

    for b in books:
        now += b[1]
        MAX = max(MAX, now)

    return MAX


print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))
