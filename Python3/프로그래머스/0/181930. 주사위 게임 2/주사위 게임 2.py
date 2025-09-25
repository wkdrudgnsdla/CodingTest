def solution(a, b, c):
    result = 0
    if a == b & b == c:
        result = (a+b+c)*(a**2+b**2+c**2)*(a**3+b**3+c**3)
    elif a != b != c != a:
        result = a + b + c
    else:
        result = (a + b+c)*(a**2+b**2+c**2)
    answer = result
    return answer