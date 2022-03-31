from collections import deque

def dfs(x):
    print(x, end=' ')
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

def bfs(x):
  visited[x] = 1
  queue = deque([x])

  while queue:
    v = queue.popleft()
    print(v, end=' ')

    for i in graph[v]:
      if not visited[i]:
        visited[i] = 1
        queue.append(i)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

dfs(V)
print()
visited = [0] * (N + 1) # dfs 후 visited 배열 초기화해준다.
bfs(V)