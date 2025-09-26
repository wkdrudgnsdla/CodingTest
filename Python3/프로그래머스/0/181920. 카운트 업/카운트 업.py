def solution(start_num, end_num):
    result = []
    idx = 0
    for i in range(end_num + 1):
        if i >= start_num:
            result.insert(idx,i)
            idx += 1
    answer = result
    return answer