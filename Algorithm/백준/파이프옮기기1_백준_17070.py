def dfs(x, y, direction):   # 좌표와 direction 변수를 입력한다. 가로 0, 세로 1, 대각선 2이다.
    global ans
    if x == n - 1 and y == n - 1:   # (n-1, n-1)에 도착하면 ans를 증가시킨다.
        ans += 1
        return

    if direction == 0 or direction == 2:    # 가로 대각선의 경우 가로로 이동한다.
        if y + 1 < n:
            if graph[x][y + 1] == 0:
                dfs(x, y + 1, 0)

    if direction == 1 or direction == 2:    # 세로 대각선의 경우 세로로 이동한다.
        if x + 1 < n:
            if graph[x + 1][y] == 0:
                dfs(x + 1, y, 1)

    if direction == 0 or direction == 1 or direction == 2:  # 가로 세로 대각선의 경우 대각선으로 이동한다.
        if x + 1 < n and y + 1 < n:     # 대각선의 경우 3 곳을 보아야한다.
            if graph[x + 1][y] == 0 and graph[x][y + 1] == 0 and graph[x + 1][y + 1] == 0:
                dfs(x + 1, y + 1, 2)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ans = 0
dfs(0, 1, 0)    # 초기 좌표와 방향을 넣어준다
print(ans)