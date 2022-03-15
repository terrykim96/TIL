from collections import deque

def bfs(start):
    queue.append(start)
    visited[start] = 1

    while queue:
        start = queue.popleft()
        
        for next in range(1, V + 1):
            if graph[start][next] and not visited[next]:
                queue.append(next)
                visited[next] = 1
                distance[next] = distance[start] + 1

                if next == end:
                    return distance[next]

    return 0

T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    visited = [0] * (V + 1)
    distance = [0] * (V + 1)
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    
    for _ in range(E):
        s, e = map(int, input().split())
        graph[s][e] = 1
        graph[e][s] = 1
    
    start, end = map(int, input().split())    
    queue = deque()

    ans = bfs(start)

    print(f'#{test_case} {ans}')