def dfs(x, depth):
    global ans
    visited[x] = 1

    if depth == 4:
        ans = 1
        return
    
    for i in friends[x]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, depth + 1)
            visited[i] = 0

N, M = map(int, input().split())
friends = [[] for _ in range(N)]
visited = [0] * N

for _ in range(M):
    a, b = map(int, input().split())
    friends[a].append(b)    # 원래 연결 상태를 1로 표현하려 했는데 시간초과 떠서 이렇게 해줌.
    friends[b].append(a)

ans = 0

for i in range(N):
    dfs(i, 0)
    visited[i] = 0

    if ans == 1:
        break

print(ans)