from collections import deque

direction_x = [-1, 1, 0, 0]
direction_y = [0, 0, -1, 1]

# 섬을 구분해주는 bfs
def bfs(x, y):
    global cnt
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    arr[i][j] = cnt

    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + direction_x[k]
            ny = y + direction_y[k]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                arr[nx][ny] = cnt
                queue.append([nx, ny])

# 바다를 건너며 가장 짧은 거리를 구한다. (bfs로 최단거리)
def route(target):
    global ans
    dist = [[-1] * N for _ in range(N)] # 거리가 저장될 배열
    queue = deque()

    for i in range(N):
        for j in range(N):  # 시작지점을 찾아준다.
            if arr[i][j] == target:
                queue.append([i, j])
                dist[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + direction_x[i]
            ny = y + direction_y[i]
            # 갈 수 없는 곳이면 continue
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            # 다른 땅을 만나면 기존 답과 비교하여 짧은 거리 선택
            if arr[nx][ny] > 0 and arr[nx][ny] != target:
                ans = min(ans, dist[x][y])
                return
            # 바다를 만나면 dist를 1씩 늘린다.
            if arr[nx][ny] == 0 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append([nx, ny])


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 1
ans = 10e6

for i in range(N):
    for j in range(N):
        if not visited[i][j] and arr[i][j] == 1:
            bfs(i, j)
            cnt += 1

for i in range(1, cnt):
    route(i)

print(ans)