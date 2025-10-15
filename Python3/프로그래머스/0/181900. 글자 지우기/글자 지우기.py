def solution(my_string, indices):
    answer = ''
    my_string_list = list(my_string)
    for i in range(len(my_string_list)):
        if not i in indices:
            answer += my_string_list[i]
    return answer