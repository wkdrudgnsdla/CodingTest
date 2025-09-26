def solution(arr, queries):
    n = len(arr)
    for s, e, k in queries:
        if s < 0: s = 0
        if e >= n: e = n - 1
        if k == 0:
            continue
        start = ((s + k - 1) // k) * k
        for i in range(start, e + 1, k):
            arr[i] += 1
    answer = arr
    return answer