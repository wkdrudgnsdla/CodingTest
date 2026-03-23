def solution(progresses, speeds):
    answer = []
    a = []
    count = 0
    counts = []
    for i in progresses:
        a.append(100 - i)
    
    for i in range(len(a)):
        while a[i] > 0:
            a[i] -= speeds[i]
            count += 1
        counts.append(count)
        count = 0
        
    maxnum = counts[0]
    fc = 1
    
    for i in range(1, len(counts) ):
        if counts[i] <= maxnum:
            fc += 1
        else:
            print(fc)
            answer.append(fc)
            fc = 1
            maxnum = counts[i]
    if fc < 1:
        answer.append(1)
    else:
        answer.append(fc)
    return answer