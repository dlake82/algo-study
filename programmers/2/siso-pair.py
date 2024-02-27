def solution(toppings):
    answer = 0
    for i in range(len(toppings) - 1):
        left, right = toppings[: i + 1], toppings[i + 1 :]
        if len(set(left)) == len(set(right)):
            answer += 1
    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2]))
