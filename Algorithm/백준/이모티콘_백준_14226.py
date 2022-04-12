from collections import deque
N = int(input())

visited = [[-1]* (N+1) for _ in range(N+1)]
queue = deque()
queue.append((1,0)) # 화면 이모티콘 개수, 클립보드 이모티콘 개수를 튜플로 큐에 넣어준다.
visited[1][0] = 0
while queue:        # bfs로 찾는다.
    s, c = queue.popleft()   # 화면에 있는 이모티콘을 꺼낸다.

    if visited[s][s] == -1: # 방문하지 않았으면
        visited[s][s] = visited[s][c] + 1   # 최단거리를 찾는 것처럼 현재 경로에 1을 더해준다.
        queue.append((s,s)) # 화면 이모티콘과 클립보드의 이모티콘 개수를 큐에 저장한다(복사).

    if s+c <= N and visited[s+c][c] == -1:    # 클립보드에 있는 이모티콘을 화면에 붙여넣는다.
        visited[s+c][c] = visited[s][c] + 1
        queue.append((s+c, c))

    if s-1 >= 0 and visited[s-1][c] == -1:    # 화면에 있는 이모티콘 중 하나를 삭제한다.
        visited[s-1][c] = visited[s][c] + 1
        queue.append((s-1, c))

ans = -1

for i in range(N + 1):
    if visited[N][i] != -1:
        if ans == -1 or ans > visited[N][i]:
            ans = visited[N][i]
print(ans)