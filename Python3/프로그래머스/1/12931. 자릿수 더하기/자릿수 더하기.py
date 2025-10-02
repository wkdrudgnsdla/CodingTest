def solution(n):
    answer = 0
    n_list = list(map(int, str(n)))
    print(n_list)
    for i in n_list:
        answer += i
    return answer