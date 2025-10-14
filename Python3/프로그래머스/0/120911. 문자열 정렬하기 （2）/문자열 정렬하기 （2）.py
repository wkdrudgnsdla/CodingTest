def solution(my_string):
    a = sorted(my_string.lower())
    answer = ''
    for ch in a:
        answer += ch
    return answer