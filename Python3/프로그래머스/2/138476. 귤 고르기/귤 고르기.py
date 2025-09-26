from collections import Counter

def solution(k, tangerine):
    counts = Counter(tangerine)
    freq = sorted(counts.values(), reverse = True)
    answer = 0
    for i in freq:
        k -= i
        answer += 1
        if k <= 0:
            break
    return answer