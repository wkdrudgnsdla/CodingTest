def solution(n, t):
    answer = 0
    for i in range(t):
        n += n
    answer = n
    return answer