from collections import Counter

def solution(a, b, c, d):
    dice = [a,b,c,d]
    count = Counter(dice)
    point = 0
    if len(count) == 1:
        p = dice[0]
        point = 1111 * p
    elif 3 in count.values():
        p = [num for num, v in count.items() if v == 3][0]
        q = [num for num, v in count.items() if v == 1][0]
        point = (10 * p + q) ** 2
    elif list(count.values()).count(2) == 2:
        p,q = count.keys()
        point = (p + q) * abs(p-q)
    elif 2 in count.values():
        p = [num for num, v in count.items() if v == 2][0]
        q, r = [num for num, v in count.items() if v == 1]
        point = q * r
    else : 
        return min(dice)
    answer = point
    return answer