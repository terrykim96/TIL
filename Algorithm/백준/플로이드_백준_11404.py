N = int(input())
M = int(input())
inf = int(10e9)

bus_cost = [[inf for _ in range(N + 1)] for _ in range(N + 1)]

# 플로이드-와샬 알고리즘을 사용한다.

for _ in range(M):
    start, end, cost = map(int, input().split())
    bus_cost[start][end] = min(cost, bus_cost[start][end])

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            
            if i == j:      # 자기 자신으로 오는 경우는 없으므로 제외해준다.
                bus_cost[i][j] = 0 
            else:           # k를 거치는 것 or 직접 가는 것을 비교하여 작은 것을 넣어준다.
                bus_cost[i][j] = min(bus_cost[i][j], bus_cost[i][k] + bus_cost[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if bus_cost[i][j] == inf:
            print(0, end=" ")

        else:
            print(bus_cost[i][j], end=" ")
    print()