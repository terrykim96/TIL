from collections import deque

dx = [0, 0, 1, -1, 1, 1, -1, -1]      # 상, 하, 좌, 우, 대각선까지 찾아준다.
dy = [1, -1, 0, 0, 1, -1, 1, -1]

def bfs(graph, a, b):   # bfs로 섬을 찾는다.
    n = len(graph)
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0     # 탐색 중 1인 부분은 0으로 바꿔 다시 방문하지 않도록 한다.
    
    while queue:
        x, y = queue.popleft()
        for d in range(8):  # 방향 리스트를 줘서 8방향 안에 갈 수 있는 곳을 찾는다.
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

while True:
    w, h = map(int, input().split())
    if not w and not h:         # 테스트 케이스 개수가 안나와있어서 구글링 했습니다..
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                bfs(graph, i, j)
                cnt += 1

    print(cnt)