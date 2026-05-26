def solution(number, k):
    answer = []

    for ch in number:
        while answer and k > 0 and answer[-1] < ch:
            answer.pop()
            k -= 1

        answer.append(ch)

    if k > 0:
        answer = answer[:-k]

    return ''.join(answer)