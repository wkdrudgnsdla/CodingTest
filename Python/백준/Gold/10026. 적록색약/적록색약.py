import copy
import sys
sys.setrecursionlimit(100000)

n = int(input())
grid = [list(input().rstrip()) for _ in range(n)]
blind_grid = copy.deepcopy(grid)

for i in range(n):
    for j in range(n):
        if grid[i][j] == "G":
            blind_grid[i][j] = "R"

visited = [[False for _ in range(n)] for _ in range(n)]

blind = False
count = 0
blind_count = 0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, color, blind):
    if x >= n or y >= n or x < 0 or y < 0: 
        return False
    if visited[x][y] == True:
        return False
    if not blind: #블라인드 아닐때
        if grid[x][y] != color:
            return False
    else: #블라인드일때
        if blind_grid[x][y] != color:
            return False
    visited[x][y] = True

    dfs(x-1, y, color, blind)
    dfs(x+1, y, color, blind)
    dfs(x, y -1, color, blind)
    dfs(x, y + 1, color, blind)
    return True



for i in range(n):
    for j in range(n):
        if dfs(i,j, grid[i][j], False) == True:
            count += 1

visited = [[False for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if dfs(i,j, blind_grid[i][j], True) == True:
            blind_count += 1

print(count, blind_count)