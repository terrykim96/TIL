from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs(arr, visited, time, S, G):
    queue = deque([S])
    while queue:
        x, y = queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if nx == 0 and ny == 0:
                    continue
                elif visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    time[nx][ny] = time[x][y] + arr[nx][ny]
                    queue.append((nx, ny))
                else:
                    if time[nx][ny] > time[x][y] + arr[nx][ny]:
                        time[nx][ny] = time[x][y] + arr[nx][ny]
                        queue.append((nx, ny))

for test_case in range(1, int(input()) + 1):
    N = int(input())
    arr = list(list(map(int, input())) for _ in range(N))

    visited = [[0] * N for _ in range(N)]
    time = [[0] * N for _ in range(N)]
    S, G = [0, 0], [N - 1, N - 1]
    
    bfs(arr, visited, time, S, G)
    ans = time[G[0]][G[1]]

    print(f'#{test_case} {ans}')