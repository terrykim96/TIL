from collections import deque

m,n = map(int,input().split())
graph = []
queue = deque([])
for i in range(n):
    graph.append(list(map(int,input().split())))
    
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j]) # 익은 토마토를 큐에 저장한다.

            
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    while queue:    # 큐가 빌 때까지 계속한다.
        x, y = queue.popleft()  # 처음 토마토 좌표를 꺼낸다.
        
        for i in range(4):      # 처음 토마토의 네 방향을 탐색하여 익힐 토마토를 찾아본다.
            a = x + dx[i]
            b = y + dy[i]

            if 0 <= a < n and 0 <= b < m and graph[a][b] == 0:  # 좌표 크기 내에 있으며 토마토가 익지 않았다면 익히고 1을 더해준다.
                queue.append([a, b])
                graph[a][b] = graph[x][y] + 1

bfs()
ans = 0
flag = True
for i in graph:
    for j in i:     # 다 찾아봤는데 토마토를 익히지 못했다면 flag를 false로 바꿔준다.
        if j == 0:
            flag = False
            break
    ans = max(ans, max(i))  # 다 익혔다면 최댓값을 정해준다.

if flag:            # flag가 true라면 정답을, false라면 -1을 출력한다.
    print(ans - 1)      # 처음 시작이 1이기 때문에 1을 빼준다.
else:
    print(-1)