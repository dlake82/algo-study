def solution(str1, str2):
    answer = 2
    l1 = len(str1)
    l2 = len(str2)
    for i in range(0, l1 - l2 + 1):
        if str1[i:i + l2] == str2:
            return 1

    return answer

solution("ab6CDE443fgh22iJKlmn1o", "6CD")