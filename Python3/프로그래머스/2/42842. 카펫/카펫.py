def solution(brown, yellow):
    answer = []
    a = brown + yellow
    for i in range(3, a):
        j = a // i
        if i * j == a and i >= j and (i - 2) * (j - 2) == yellow:
            answer.append(i)
            answer.append(j)
            return answer
