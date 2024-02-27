from collections import deque


def solution(picks, minerals):
    pm_table = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]

    dia, iron, stone = picks
    tired, works, di, ir, st = 0, deque(), "diamond", "iron", "stone"

    ps = deque([0] * dia + [1] * iron + [2] * stone)
    pl, ml = len(ps), len(minerals)
    minerals = minerals[0:pl * 5 if pl * 5 < ml else ml]

    for i, m in enumerate(minerals):
        idx, pi = i % 5, i // 5

        if idx == 0:
            works.append([0, 0, 0])
        works[pi][0] += 1 if m == di else 0
        works[pi][1] += 1 if m == ir else 0
        works[pi][2] += 1 if m == st else 0

    works = list(
        reversed(sorted(list(works), key=lambda x: (x[0], x[1], x[2]))))

    for p, work in zip(ps, works):
        for m, w in enumerate(work):
            tired += (pm_table[p][m] * w)

    return tired


print(solution([1, 3, 2], ["diamond", "diamond", "diamond",
      "iron", "iron", "diamond", "iron", "stone"]))
