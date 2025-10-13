def solution(my_string, n):
    answer = ''
    s_list = list(my_string[::-1])
    for i in range(len(s_list)):
        if i < n:
            answer += s_list[i]
    return answer[::-1]