from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    n = len(words)
    visited = [False] * n
    q = deque([(begin, 0)])

    while q:
        cur, steps = q.popleft()
        if cur == target:
            return steps
        for i in range(n):
            if visited[i]:
                continue
            diff = sum(1 for a, b in zip(cur, words[i]) if a != b)
            if diff == 1:
                visited[i] = True
                q.append((words[i], steps + 1))
    return 0
