inf = int(10e9)

# 벨만 포드 알고리즘 사용

def bellman_ford(start):
    dist[start] = 0

    # N번의 라운드를 반복한다.
    for i in range(1, N + 1):
        # 매 라운드마다 모든 간선을 확인해서
        for j in range(M):
            now, next, cost = edges[j][0], edges[j][1], edges[j][2]

            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 간선의 거리를 갱신한다.
            if dist[now] != inf and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost

                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재하는 것이다.
                if i == N:
                    return True

    return False


N, M = map(int, input().split())
edges = []
dist = [inf] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

negative_cycle = bellman_ford(1)

if negative_cycle:
    # 음수 순환이 존재하면 -1을 출력한다.
    print(-1)

else:
    for i in range(2, N + 1):
        # 도달할 수 없는 경우 -1을 출력한다.
        if dist[i] == inf:
            print(-1)

        # 도달 가능한 경우 최단거리를 출력한다.
        else:
            print(dist[i])