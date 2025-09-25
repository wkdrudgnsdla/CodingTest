def solution(my_string, alp):
    result_string = ""
    for i in range(len(my_string)):
        if my_string[i] == alp:
            result_string += my_string[i].upper()
        else:
            result_string += my_string[i]
    answer = result_string
    return answer