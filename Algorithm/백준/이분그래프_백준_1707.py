from collections import deque

def bfs(graph, start):
    global ans

    queue = deque()
    queue.append(start)
    if visited[start] == 0:
        visited[start] = 1  # 이분은 1, 2로 하고 아직 방문하지 않은곳은 0으로 표시
    
    while queue:
        v = queue.popleft()

        color = visited[v]
        for i in graph[v]:  # V정점과 연결된 모든 정점 확인
            if visited[i] == 0:  # 아직 한번도 방문하지 않음
                queue.append(i)  # 다음에 방문할 곳으로 지정
                if color == 1:  # 현재의 정점과 다른 색상으로 색칠
                    visited[i] = 2
                else:
                    visited[i] = 1
            elif visited[i] == 1:
                if color == 1:
                    ans = 'NO'
                    return
            elif visited[i] == 2:
                if color == 2:
                    ans = 'No'
                    return 
    return

T = int(input())
for _ in range(T):
    ans = 'YES'
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for i in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1, V + 1): # 연결그래프일 경우에는 시작점에서 한번의 BFS를 수행하면 되지만 비연결그래프의 경우에는 모든 정점을 탐색해야 한다.
        bfs(graph, i)
        if ans == 'No':
            break
    
    print(ans)