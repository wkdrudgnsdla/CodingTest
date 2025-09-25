def solution(numLog):
    resultStr = ""
    for i in range(len(numLog) - 1):
        diff = numLog[i+1] - numLog[i] 
        if diff == 1:
            resultStr += "w"
        elif diff == -1:
            resultStr += "s"
        elif diff == 10:
            resultStr += "d"
        elif diff == -10:
            resultStr += "a"
    return resultStr
