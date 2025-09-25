def solution(n):
    result = [n]
    idx = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2;
            result.insert(idx, n)
            idx +=1
        elif n % 2 != 0:
            n = 3 * n + 1
            result.insert(idx, n)
            idx += 1
    answer = result
    return answer