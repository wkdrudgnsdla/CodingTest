def solution(arr, k):
    result = []
    if k % 2 == 0:
        for i in range(len(arr)):
            result.insert(i, arr[i] + k)
    elif k % 2 != 0:
        for i in range(len(arr)):
            result.insert(i, arr[i] * k)
    answer = result
    return answer