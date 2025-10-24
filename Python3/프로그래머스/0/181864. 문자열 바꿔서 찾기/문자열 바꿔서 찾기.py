def solution(myString, pat):
    answer = ""
    l = list(myString)
    for ch in l:
        if ch == "A":
            answer += "B"
        elif ch == "B":
            answer += "A"
            
    if pat in answer:
        return 1
    else:
        return 0