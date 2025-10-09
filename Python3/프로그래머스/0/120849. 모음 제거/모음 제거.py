def solution(my_string):
    answer = []
    list_string = list(my_string)
    for ch in list_string:
        if ch == "a":
            continue
        elif ch == "e":
            continue
        elif ch == "i":
            continue
        elif ch == "o":
            continue
        elif ch == "u":
            continue
        else:
            answer.append(ch)
    return "".join(answer)