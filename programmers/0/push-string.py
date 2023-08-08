def solution(num, k):
    txt = str(num)
    
    for i in range(len(txt)):
        target = txt[i]
        # print(target)
        if target == str(k):
            return i + 1

    return -1

print(solution(232443,4))
