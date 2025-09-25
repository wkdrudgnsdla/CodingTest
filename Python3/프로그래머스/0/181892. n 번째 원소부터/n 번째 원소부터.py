def solution(num_list, n):
    a = 0
    result = []
    for i in range(len(num_list)):
        if i >= n-1:
            result.insert(a , num_list[i])
            a += 1
    answer = result
    print(result)
    return answer