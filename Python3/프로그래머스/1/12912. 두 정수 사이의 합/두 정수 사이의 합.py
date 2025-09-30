def solution(a, b):
    answer = 0
    answer = sum(range(a, b + 1))
    if answer == 0:
        answer = sum(range(b, a + 1))
    return answer