from collections import deque

def bfs(start):
    queue = deque([start])
    cnt = 1
    room[maps[start[0]][start[1]]] = 0

    while queue:
        i, j = queue.popleft()

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if 0 <= ni < N and 0 <= nj < N and maps[ni][nj] == maps[i][j] + 1:
                queue.append([ni, nj])
                cnt += 1
                room[maps[ni][nj]] = 0

    return cnt
 
 
T = int(input())
 
di = [1, -1, 0, 0]
dj = [0, 0, -1, 1]
 
for test_case in range(1, T + 1):
    N = int(input())
    maps = [list(map(int, input().split())) for _ in range(N)]
    room = [0] * (N ** 2 + 1)
    
    for i in range(N):
        for j in range(N):
            room[maps[i][j]] = [i, j]
 
    ans = 0
    idx = 0
 
    for i in range(1, len(room)):
        loc = room[i]
        if loc != 0:
            tmp = bfs(room[i])
            if ans < tmp:
                ans = tmp
                idx = i
    
    print(f'#{test_case} {idx} {ans}')