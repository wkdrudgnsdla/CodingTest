def solution(strArr):
    answer = []
    for ch in strArr:
        if not "ad" in ch:
            answer.append(ch)
    return answer