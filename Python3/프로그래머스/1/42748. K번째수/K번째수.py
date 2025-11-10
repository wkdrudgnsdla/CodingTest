def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        arr = array[commands[i][0]-1:commands[i][1]]
        arr.sort()
        n = commands[i][2]
        answer.append(arr[n-1])
    return answer