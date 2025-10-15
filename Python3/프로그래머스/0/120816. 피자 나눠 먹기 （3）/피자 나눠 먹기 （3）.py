def solution(slice, n):
    import math
    answer = 0
    if slice % n == 0:
        answer = 1
    else:
        answer = math.ceil(n/slice)
    return answer