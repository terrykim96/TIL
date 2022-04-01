T = int(input())
for test_case in range(1, T + 1):
    V, E = map(int, input().split())
    adj = {i: [] for i in range(V+1)}
    for i in range(E):
        s, e, c = map(int, input().split())
        adj[s].append([e, c])

    
    dist = [10e6] * (V+1)
    selected = [0] * (V+1)

    dist[0] = 0
    cnt = 0
    while cnt < (V):
        min_val = 10e6
        u = -1
        for i in range(V + 1):
            if not selected[i] and dist[i] < min_val:
                min_val = dist[i]
                u = i
        # 결정
        selected[u] = 1
        cnt += 1
        # 간선완화
        for w, cost in adj[u]:  # 도착정점, 가중치
            if dist[w] > dist[u] + cost:
                dist[w] = dist[u] + cost

    print(f'#{test_case} {dist[V]}')