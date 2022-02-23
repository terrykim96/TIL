for _ in range(1, 11):
    test_case, V = map(int, input().split())
    lst = list(map(int, input().split()))
    adj = [[] for _ in range(100)]
    visited = [0] * 100
    visited[0] = 1

    for i in range(0, len(lst), 2):
        adj[lst[i]].append(lst[i + 1])
    
    ans = 0
    stk = [0]
    while stk:
        c = stk.pop()
        for neighbor in adj[c]:
            if neighbor == 99:
                ans = 1
                break
            if not visited[neighbor]:
                stk.append(neighbor)
                visited[neighbor] = 1
    print(f'#{test_case} {ans}')