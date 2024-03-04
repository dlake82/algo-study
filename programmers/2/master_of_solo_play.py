def solution(cards):
    cards = list(map(lambda x: x-1, cards))
    visited = [False for _ in cards]
    groups = []

    for i, card in enumerate(cards):
        if not visited[i]:
            visited[i] = True
            group_count = 1

            while True:
                if not visited[card]:
                    visited[card] = True
                    card = cards[card]
                    group_count += 1
                else:
                    break

            groups.append(group_count)

    groups.sort(reverse=True)

    return groups[0] * groups[1] if len(groups) > 1 else 0


print(solution([8, 6, 3, 7, 2, 5, 1, 4]))
