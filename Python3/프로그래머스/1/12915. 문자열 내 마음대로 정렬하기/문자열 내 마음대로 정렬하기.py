def solution(strings, n):
    answer = []
    arr = []
    for i in range(len(strings)):
        arr.append(strings[i][n:n+1])
    
    arr2 = []
    for i in range(len(arr)):
        arr2.append((arr[i], strings[i]))
        
    arr2.sort()
    
    for key, word in arr2:
        answer.append(word)
    return answer