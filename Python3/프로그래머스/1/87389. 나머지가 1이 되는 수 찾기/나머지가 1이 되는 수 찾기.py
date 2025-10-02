def solution(n):
    answer = 0
    for i in range(n):
        answer += 1
        if n % answer == 1:
            break
    return answer