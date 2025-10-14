def solution(my_string):
    number = ["1","2","3","4","5","6","7","8","9","0"]
    answer = []
    my_string_list = list(my_string)
    for ch in my_string_list:
        if ch in number:
            answer.append(int(ch))
    return sorted(answer)