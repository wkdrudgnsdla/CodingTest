from collections import deque

x, y = map(int, input().split())
arr = []
for i in range(y):
    arr.append(list(map(int, input().split())))

queue = deque()

for i in range(y):
    for j in range(x):
        if arr[i][j] == 1:
            queue.append([i, j])

dx = [-1, 1, 0, 0] 
dy = [0, 0, -1, 1] 

while queue:
    now_i, now_j = queue.popleft()
    
    for i in range(4):
        nx = now_i + dx[i]
        ny = now_j + dy[i]
        
        if 0 <= nx < y and 0 <= ny < x and arr[nx][ny] == 0:
            arr[nx][ny] = arr[now_i][now_j] + 1
            queue.append([nx, ny])

flag = 0
date = 0
for i in range(y):
    for j in range(x):
        if arr[i][j] == 0: 
            flag = 1
        date = max(date, arr[i][j])

print(-1 if flag else date - 1)