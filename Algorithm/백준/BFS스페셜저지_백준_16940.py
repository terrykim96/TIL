from collections import deque


def bfs(x):
    visited = [0] * (N + 1)
    queue = deque([x])
    ans = [1]
    visited[x] = 1

    while queue:
        v = queue.popleft()
        
        for node in graph[v]:
            if not visited[node]:
                queue.append(node)
                visited[node] = 1
                ans.append(node)
    
    return ans

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

path = list(map(int, input().split()))

order = [0] * (N + 1)

for i in range(N):      # order 리스트에 노드 우선순위를 담는다.
    order[path[i]] = i + 1

for i in range(1, N + 1):   # 그래프 인접 요소를 order 리스트 값에 따라 바꿔준다.
    graph[i].sort(key= lambda x : order[x])

bfs(1)