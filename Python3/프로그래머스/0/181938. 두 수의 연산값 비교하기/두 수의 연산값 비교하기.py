def solution(a, b):
    result1 = int(str(a) + str(b))
    result2 = 2 * a * b
    if result2 > result1:
        answer = result2
    else:
        answer = result1
    return answer