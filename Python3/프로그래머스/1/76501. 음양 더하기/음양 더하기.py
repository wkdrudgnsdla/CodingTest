def solution(absolutes, signs):
    answer = 123456789
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] *= -1;
        else:
            absolutes[i] = absolutes[i]
    answer = sum(absolutes)
    return answer