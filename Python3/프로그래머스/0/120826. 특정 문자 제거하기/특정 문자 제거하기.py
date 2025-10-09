def solution(my_string, letter):
    return "".join([i for i in my_string if not(i in letter)])