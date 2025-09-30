def solution(s):
    answer = ''
    idx = 0
    for i, ch in enumerate(s):
        if ch == ' ':
            answer += ch
            idx = 0
        else:
            if idx % 2 == 0:
                answer += ch.upper()
                idx += 1
            else:
                answer += ch.lower()
                idx += 1
    return answer