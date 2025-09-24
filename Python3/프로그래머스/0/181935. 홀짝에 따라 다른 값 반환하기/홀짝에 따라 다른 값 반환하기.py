def solution(n):
    result1 = 0
    result2 = 0
    if n % 2 != 0:
        for i in range(n + 1):
            if i % 2 != 0:
                result1 += i
        answer = result1
    else:
        for i in range(n + 1):
            if i %2 == 0:
                result2 += i * i
        answer = result2
    
    return answer