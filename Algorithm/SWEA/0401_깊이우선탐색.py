def dfs(x):
    ans.append(x)
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

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
    dfs(1)

    print(f'#{test_case}', *ans)