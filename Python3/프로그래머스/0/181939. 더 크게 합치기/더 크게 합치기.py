def solution(a, b):
    result = 0
    result2 = 0
    result = int(str(b) + str(a))
    result2 = int(str(a) + str(b))
    if result < result2 :
        answer = result2
    else:
        answer = result
    return answer