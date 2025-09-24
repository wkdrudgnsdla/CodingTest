def solution(num, n):
    result = num % n
    if result == 0:
        answer = 1
    else:
        answer = 0
    return answer