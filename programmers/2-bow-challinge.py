from collections import Counter

def solution(a, b, c, d):
    arr = [a, b, c, d]
    c = Counter(arr)
    l = len(c)
    ks = c.keys()
    Counter.most_common
    
    if l == 1:
        return 1111 * a
    elif l == 2:
        fv = c[ks[0]]
        if fv == 3:
            return (10 * p + q) ** 2
        if fv == 2:
            return (p + q) * abs(p - q)
    elif l == 3:
        r = c[list(ks)[2]]
        return q * r
    else:
        return min(arr)
