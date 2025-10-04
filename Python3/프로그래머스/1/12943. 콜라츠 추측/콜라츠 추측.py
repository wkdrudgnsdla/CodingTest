def solution(num):
    answer = 0
    count = 0
    if num == 1:
        answer = 0
    while num != 1:
        if count == 500:
            answer = -1
            break
        else:
            if num % 2 == 0:
                num /= 2
                count += 1
                answer = count
            else:
                num = num * 3 + 1
                count += 1
                answer = count
    return answer