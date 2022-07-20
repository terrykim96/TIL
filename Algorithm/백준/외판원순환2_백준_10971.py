import sys
input = sys.stdin.readline

N = int(input())




cities = []

for _ in range(N):
    cities.append(list(map(int, input().split())))


ans = 10e7


visited = [0] * N

def dfs(start, depth, cost):
    global  cities, visited, ans

    if start == depth and visited.count(0) == 0:      # 다 돌았을때
        ans = min(ans, cost)


    for i in range(N):      # 전체를 다 dfs로 돌면서 가장 작은 값을 찾는다.
        if not cities[depth][i] == 0 and not visited[i]:
            visited[i] = 1
            dfs(start, i, cost + cities[depth][i])
            visited[i] = 0

dfs(0, 0, 0)
print(ans)