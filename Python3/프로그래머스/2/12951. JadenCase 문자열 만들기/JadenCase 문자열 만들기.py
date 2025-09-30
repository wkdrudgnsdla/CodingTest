def solution(s):
    answer = ''
    s_list = s.split(" ")
    for i in range(len(s_list)):
        if s_list[i] == ' ':
            answer += ' '
        else:
            answer += s_list[i].capitalize()
        if i+ 1 != len(s_list):
            answer += ' '
    return answer