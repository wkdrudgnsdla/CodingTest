def solution(num_list):
    result_list = num_list
    if num_list[-1] > num_list[-2]:
        result_list.append(num_list[-1] - num_list[-2])
    else:
        result_list.append(num_list[-1] * 2)
    answer = result_list
    return answer