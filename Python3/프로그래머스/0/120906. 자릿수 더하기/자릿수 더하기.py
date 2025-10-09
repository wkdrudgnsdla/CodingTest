def solution(n):
    nlist = list(map(int, str(n)))
    answer = 0
    for i in nlist:
        answer += int(i)
    return answer