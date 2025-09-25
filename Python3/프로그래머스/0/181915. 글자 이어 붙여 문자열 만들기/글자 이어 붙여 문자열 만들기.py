def solution(my_string, index_list):
    result = ""
    for idx in index_list:
        result += my_string[idx]
    return result