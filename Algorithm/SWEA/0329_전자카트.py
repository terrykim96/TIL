# (current, next) = 0,1 -> 1,2 -> 2,0
def dfs(current, tmp):
    global ans
    if tmp < ans:
        if 0 not in visited[1:]:  # 전부 방문했다면
            ans = min(ans, tmp + a[current][0])  # 결과값 갱신하고 함수 종료
            return
        for next in range(1, N):
            if a[current][next] != 0 and visited[next] == 0:
                visited[next] = 1
                dfs(next, tmp + a[current][next])
                visited[next] = 0

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a = [list(map(int, input().split())) for _ in range(N)]

    ans = 10000
    for i in range(1, N):
        visited = [0] * N
        visited[i] = 1
        dfs(i, a[0][i])  # current_y, tmp_sum

    print(f'#{test_case} {ans}')