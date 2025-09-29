def solution(x):
    answer = True
    num = 0
    x_list = list(map(int, str(x)))
    for i in range(len(x_list)):
        num += x_list[i]
    if x % num == 0:
        answer = True
    else:
        answer = False
    return answer