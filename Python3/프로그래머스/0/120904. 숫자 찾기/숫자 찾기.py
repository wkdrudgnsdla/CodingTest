def solution(num, k):
    answer = 0
    list_n = list(str(num))
    if str(k) in list_n:
        answer = list_n.index(str(k)) + 1
    else:
        answer = -1
    return answer