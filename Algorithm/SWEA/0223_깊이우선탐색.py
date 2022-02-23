T = int(input())

for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = [[0]*(V+1) for _ in range(V+1)]
    visited = [0] * (V+1)
    stk = [1]
    visited[1] = 1
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj[n1][n2] = 1
        adj[n2][n1] = 1

    ans = [1]
    s = 1
    while stk:
        for i in range(1, V+1):
            if not visited[i] and adj[s][i]:
                stk.append(i)
                visited[i] = 1
                ans.append(i)
                s = i
                break
        else:
            s = stk.pop()
            
    print(f'#{test_case}', *ans)