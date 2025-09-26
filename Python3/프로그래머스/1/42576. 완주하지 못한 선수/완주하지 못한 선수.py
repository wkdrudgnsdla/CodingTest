from collections import Counter

def solution(participant, completion):
    diff = Counter(participant) - Counter(completion)
    answer = next(iter(diff))
    return answer