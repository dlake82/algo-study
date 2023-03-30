def solution(num, total):
    answer = []

    if total == 0:
        for i in range(-(num // 2), (num // 2) + 1):
            answer.append(i)
    
    for i in range(total, 0, -1):
        print(i)
        SUM = 0
        for j in range(num):
            now = i - j
            SUM += now
        print(SUM, total)
            
        if SUM == total:
            for k in range(num):
                answer.append(i - num + k + 1)
            return answer
    
    return answer

ret = solution(3, 0)
print(ret)