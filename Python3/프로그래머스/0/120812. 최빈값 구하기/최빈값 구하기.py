from collections import Counter

def solution(array):
    answer = 0
    count = Counter(array).most_common()
    if len(count) > 1 and count[0][1] == count[1][1]:
       return -1
    else:
       return count[0][0]
