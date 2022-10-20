direction_i = [0, 0, -1, 1]
direction_j = [-1, 1, 0, 0]

cnt = {}

def dfs(i, j, area, n, dep):

    if area[i][j] == 2:
        return

    area[i][j] = 1
    dep = 1

    for d in range(4):
        ni = i + direction_i[d]
        nj = j + direction_j[d]
        
        if 0 <= ni < n and 0 <= nj < n and area[ni][nj] == 0:
            dfs(ni, nj, area, n, dep)
            cnt[str(area)] = 1




def solution(n, water):
    ans = 0
    
    area = [[0]*n for _ in range(n)]

            

    for i in range(len(water)):
        x, y = water[i]
        area[x-1][y-1] = 2

    for i in range(n):
        for j in range(n):
            dfs(i, j, area, n, ans)

    print(len(cnt))
    return len(cnt)

solution(4, [[1, 2], [2, 2]])