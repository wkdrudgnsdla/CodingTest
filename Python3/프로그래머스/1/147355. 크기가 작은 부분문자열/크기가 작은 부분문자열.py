def solution(t, p):
    answer = 0
    t = list(t)
    for i in range(len(t) - len(p) + 1):
        string = ""
        for j in range(len(p)):
            string += t[i+j]
                
        if string <= p:
                answer += 1
    return answer