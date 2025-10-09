def solution(my_string, n):
    answer = ''
    list_string = list(my_string)
    for ch in list_string:
        answer += ch * n
    return answer