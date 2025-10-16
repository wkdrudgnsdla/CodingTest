def solution(n, s):
    answer = [s//n] * (n-s%n)
    answer2 = [(s//n)+1] * (s%n)
    if s // n == 0:
        return [-1]
    answer.extend(answer2)
    return answer