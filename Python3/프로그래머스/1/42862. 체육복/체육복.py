def solution(n, lost, reserve):
    were = []

    for i in range(1, n + 1):
        if i not in lost or i in reserve:
            were.append(i)

    for i in range(1, n + 1):
        if i in were and i in reserve and i not in lost:
            if i - 1 >= 1 and i - 1 not in were:
                were.append(i - 1)
            elif i + 1 <= n and i + 1 not in were:
                were.append(i + 1)

    return len(were)