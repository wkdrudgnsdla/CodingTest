def solution(s):
    answer = 0
    buho = 1
    if s in '-':
        s.delete('-')
        buho = -1
    elif s in '+':
        s.delete('+')
        buho = 1
    answer = int(s)
    if buho == 1:
        answer = answer
    elif buho == -1:
        answer *= -1
    return answer