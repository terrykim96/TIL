from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(graph, a, b):   # bfs로 단지를 찾는다.
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0     # 탐색 중 1인 부분은 0으로 바꿔 다시 방문하지 않도록 한다.
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for d in range(4):  # 방향 리스트를 줘서 네방향 안에 갈 수 있는 곳을 찾는다.
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1    # 단지의 넓이를 구해야 하므로 cnt를 1씩 늘려준다.
    return cnt


N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

cnt = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:    # 전체 그래프를 돌면서 1인 지점부터 찾기 시작한다.
            cnt.append(bfs(graph, i, j))

cnt.sort()                  # 단지 크기를 오름차순으로 배열한다.

print(len(cnt))
for i in range(len(cnt)):
    print(cnt[i])