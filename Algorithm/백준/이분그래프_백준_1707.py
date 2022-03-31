'''from collections import deque

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
                    ans = 'NO'
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
        if ans == 'NO':
            break
    
    print(ans)'''



from collections import deque
import sys
#sys.stdin = open("1707.in", "r")

def dfs(i):
    global correct, dpt
    # print('초기점 : ',p)
    # print('깊이 : ',dpt)
    # print(visited)
    for k in range(len(adj[i])):
        if visited[adj[i][k]] == 0:
            visited[adj[i][k]] = 1
            dpt += 1
            dfs(adj[i][k])

        # 다시 초기점으로 돌아왔을 때,
        # 홀수각형 사이클이면 이분 불가능
        elif adj[i][k] == p and dpt > 2:
            if dpt % 2 == 1:
                correct = 1
                return
            
    else:
        # 바로 전 노드로 돌아갈 때, 깊이 1 감소. 마지막 방문했던 노드 초기화.
        dpt -= 1
        return

K = int(input())
for _ in range(K):
    N, M = map(int, sys.stdin.readline().split())
    adj = deque()
    for _ in range(N+1):
        adj.append([])
    for _ in range(M):
        a,b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    
    correct = 0

    for p in range(N+1):
        visited = [0] * (N+1)
        if sum(adj[p]) != 0 and visited[p] == 0:
            visited[p] = 1
            dpt = 1
            dfs(p)
            if correct == 1:
                print('NO')
                break
    else:
        print('YES')