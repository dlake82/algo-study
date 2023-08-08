from collections import defaultdict

def solution(s):
    answer = ''

    d = defaultdict(int)
    for key in list(s):
        if not d[key]:
            d[key] = 0
        
        d[key] += 1
    
    for k, v in d.items():
        if v == 1:
            answer += k
    

    return answer

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"]	))
