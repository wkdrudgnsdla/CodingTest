import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    a = abs(denom1 * denom2) // math.gcd(denom1, denom2)
    b = [numer1 * (a // denom1), numer2 * (a // denom2)]
    
    answer = [b[0] + b[1], a]
    c = math.gcd(answer[0], answer[1])
    return [answer[0] // c, answer[1] // c]