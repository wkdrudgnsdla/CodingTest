def solution(number, limit, power):
    answer = 0
    arr = []
    for i in range(1,number + 1):
        count = 0
        if i == 1:
            arr.append(1)
        else:
            for j in range(1, int(i**0.5)+1):
                if i % j == 0:
                    count += 1
                    if j ** 2 != i:
                        count += 1
            arr.append(count)
            
    for k in arr:
        if k > limit:
            answer += power
        else:
            answer += k
    return answer