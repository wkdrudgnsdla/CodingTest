def solution(numbers):
    answer = []
    n_list = sorted(numbers)
    for i in range(len(n_list)):
        for j in range(1, len(n_list)):
            hap = n_list[i] + n_list[j]
            if i != j:
                if not hap in answer:
                    answer.append(hap)
    return sorted(answer)