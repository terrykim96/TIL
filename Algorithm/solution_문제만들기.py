from itertools import combinations
T = int(input())
N, M = map(int, input().split())

st, ed = 0, 0
H = []
area = []

for r in range(N):
    row = list(map(int, input().split()))
    for c in range(N):
        if row[c]:
            if not st and row[c] == 3:
                st = (r, c)
            elif not ed and row[c] == 2:
                ed = (r, c)
        else:
            area.append((r, c))    
    H.append(row)
            

def sol(map, chair):
    tmp = [[0]*N for _ in range(N)]
    d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    Q = [(st)]
    ex, ey = ed
    
    while Q:
        x, y = Q.pop(0)
        if tmp[ex][ey] and tmp[x][y] >= tmp[ex][ey]:
            continue
        ci = 3 if (x, y) in chair else 1
    
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0<= nx < N and 0<= ny < N and map[nx][ny] != 1:
                if tmp[nx][ny]:
                    if tmp[x][y] + ci >= tmp[nx][ny]:
                        continue
                tmp[nx][ny] = tmp[x][y] + ci
                if (nx, ny) == ed:
                    continue
                Q.append((nx, ny))

    return tmp[ex][ey]
    
ans = 0

for comb in combinations(area, M):
    tmp = sol(H, comb)
    if tmp > ans:
        ans = tmp
    if ans >= T or not tmp:
        print('SAFE')
        break
else:
    print(f'GOOD LUCK {T-ans}')