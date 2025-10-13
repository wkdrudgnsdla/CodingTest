def solution(s):
    answer = []
    last_pos = {}
    for i, ch in enumerate(s):
        if ch not in last_pos:
            answer.append(-1)
        else:
            answer.append(i - last_pos[ch])
        last_pos[ch] = i
    return answer