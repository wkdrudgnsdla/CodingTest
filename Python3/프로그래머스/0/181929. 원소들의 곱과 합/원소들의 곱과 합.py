def solution(num_list):
    x = 1
    xx = 0
    for i in range(len(num_list)):
        x *= num_list[i]
        xx += num_list[i]
    xx **= 2
    print(x)
    print(xx)
    if x > xx:
        answer = 0
    elif x < xx:
        answer = 1
    return answer