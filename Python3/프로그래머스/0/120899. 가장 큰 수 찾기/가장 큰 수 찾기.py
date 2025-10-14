def solution(array):
    answer = []
    big = 0
    for i in array:
        if i > big:
            big = i
    answer.append(big)
    answer.append(array.index(big))
    return answer