def solution(m, n, puddles):
    answer = 0
    area = []
    
    for i in range(n):
        area.append([])
        for j in range(m):
            area[i].append(0)
    
    # 물웅덩이 표시
    for puddle in puddles:
        x = puddle[0] - 1
        y = puddle[1] - 1
        area[y][x] = -1
    
    # 시작점
    area[0][0] = 1
    
    for i in range(n):
        for j in range(m):
            # 물웅덩이면 지나갈 수 없음
            if area[i][j] == -1:
                area[i][j] = 0
                continue
            
            # 시작점은 이미 1 넣었으니까 넘김
            if i == 0 and j == 0:
                continue
            
            # 위에서 오는 경우
            if i > 0:
                area[i][j] += area[i - 1][j]
            
            # 왼쪽에서 오는 경우
            if j > 0:
                area[i][j] += area[i][j - 1]
            
            area[i][j] %= 1000000007
    
    answer = area[n - 1][m - 1]
    return answer