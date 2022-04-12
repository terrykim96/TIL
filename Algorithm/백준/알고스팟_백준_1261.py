from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

M, N = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]  # 거리

queue = deque()
queue.append((0,0))
dist[0][0] = 0

while queue:            # bfs로 최단거리를 찾는 방법과 거의 유사하다.
    x,y = queue.popleft()
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if dist[nx][ny] == -1:          # 가보지 않았다면
                if arr[nx][ny] == 0:        # 빈 방이라면 appendleft 해준다.
                    dist[nx][ny] = dist[x][y]
                    queue.appendleft((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
print(dist[N-1][M-1])