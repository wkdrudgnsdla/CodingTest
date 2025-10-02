def solution(n):
    answer = 0
    c = n & -n
    r = n + c
    answer =  r | (((r ^ n) // c) >> 2)
            
    return answer