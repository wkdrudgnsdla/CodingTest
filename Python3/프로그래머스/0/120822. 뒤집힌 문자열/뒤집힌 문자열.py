def solution(my_string):
    answer = ''
    reverse_list = list(reversed(my_string))
    for ch in reverse_list:
        answer += ch
    return answer