def solution(my_string):
    answer = ''
    my_string_list = list(my_string)
    for ch in my_string_list:
        if ch.isupper():
            answer += ch.lower()
        else:
            answer += ch.upper()
    return answer