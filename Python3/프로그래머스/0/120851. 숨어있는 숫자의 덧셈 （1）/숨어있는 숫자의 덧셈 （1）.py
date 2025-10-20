def solution(my_string):
    answer = 0
    num = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    for ch in my_string:
        if ch in num:
            answer += int(ch)
    return answer