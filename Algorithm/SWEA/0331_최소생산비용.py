def dfs(x, depth):
    global ans
    if depth >= ans:
        return
    if x == N:
        ans = depth
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            dfs(x + 1, depth + V[x][i])
            visited[i] = 0
 
T = int(input()) 
for test_case in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    ans = 10e6

    dfs(0, 0)

    print(f'#{test_case} {ans}')