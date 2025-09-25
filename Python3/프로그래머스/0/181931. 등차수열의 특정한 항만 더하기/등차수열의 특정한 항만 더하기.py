def solution(a, d, included):
    total = 0
    for i in range(len(included)):
        term = a + d * i  
        if included[i]:
            total += term
    return total
