def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    a, b = 1, 2
    for _ in range(3, n+1):
        a, b = b, (a+b) % 1234567
    return b