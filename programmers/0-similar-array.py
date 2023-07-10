from copy import deepcopy

def solution(s1, s2):
    answer = 0

    s1 = deepcopy(list(set(s1)))
    s2 = deepcopy(list(set(s2)))

    print(s1, s2)

    return answer

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]	))