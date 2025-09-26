def solution(arr, queries):
    ans = []
    for s, e, k in queries:
        best = None  
        for i in range(s, e+1):
            val = arr[i]
            if val > k:
                if best is None or val < best:
                    best = val
        ans.append(best if best is not None else -1)
    return ans

arr = [0, 1, 2, 4, 3]
queries = [[0,4,2],[0,3,2],[0,2,2]]
print(solution(arr, queries)) 