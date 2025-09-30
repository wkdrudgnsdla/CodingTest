def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 != 0:
            answer += '박'
        elif i % 2 == 0:
            answer += '수'
    return answer