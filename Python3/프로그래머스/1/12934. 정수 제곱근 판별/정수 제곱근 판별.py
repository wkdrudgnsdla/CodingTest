import math

def solution(n):
    answer = math.sqrt(n)
    answer = n ** 0.5
    if int(answer) == answer:
        answer = (answer + 1) ** 2
    else:
        answer = -1
    return answer