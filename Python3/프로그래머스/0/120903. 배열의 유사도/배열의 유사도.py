def solution(s1, s2):
    answer = 0
    for ch in s2:
        if ch in s1:
            answer += 1
        
    return answer