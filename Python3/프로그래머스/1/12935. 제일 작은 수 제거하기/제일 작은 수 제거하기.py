def solution(arr):
    answer = arr
    min_num = 10000
    for i in arr:
        if i < min_num:
            min_num = i
    answer.remove(min_num)
    if len(answer) == 0:
        answer.append(-1)
    return answer