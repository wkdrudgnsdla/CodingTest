def solution(name, yearning, photo):
    answer = []
    for i in range(len(photo)):
        point = 0
        for j in range(len(photo[i])):
            if photo[i][j] in name:
                point += yearning[name.index(photo[i][j])]
        answer.append(point)
    return answer