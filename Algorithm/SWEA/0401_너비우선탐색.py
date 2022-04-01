from collections import deque

def bfs(x):

  visited[x] = 1
  queue = deque([x])

  while queue:
    v = queue.popleft()
    ans.append(v)

    for i in graph[v]:
      if not visited[i]:
        visited[i] = 1
        queue.append(i)

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    visited = [0] * (V + 1)
    graph = [[] for _ in range(V + 1)]
    
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = []
    bfs(1)

    print(f'#{test_case}', *ans)