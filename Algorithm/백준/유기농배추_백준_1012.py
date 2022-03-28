import sys
sys.setrecursionlimit(10**6)    # Recursion 에러가 발생해서 최대 깊이를 늘려준다.

def search(x, y):    # 배추 찾는 알고리즘(재귀를 이용한다.)
    if x < 0 or x >= M or y < 0 or y >= N:
        return

    if graph[x][y] == 0:
        return

    graph[x][y] = 0 # 탐색한 배추는 0으로 갱신한다.

    # 동서남북 탐색
    search(x + 1, y)
    search(x, y + 1)
    search(x - 1, y)
    search(x, y - 1)

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]

    result = 0 # 지렁이 수

    for _ in range(K): # 밭 정보를 graph에 저장한다.
        a, b = map(int,input().split())
        graph[b][a] = 1

    for i in range(M):      # 밭 전체를 탐색하면서
        for j in range(N):
            if graph[i][j] == 1: # 배추가 존재하는 경우 인접 배추를 탐색하고 search가 끝나면 지렁이 수를 추가한다.
                search(i, j)
                result += 1

    print(result)