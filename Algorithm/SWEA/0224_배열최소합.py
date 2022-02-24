def find_min(n, tmp):    
    global minimum

    if minimum < tmp:
        return

    if n == N:
        if minimum > tmp:
            minimum = tmp

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find_min(n+1, tmp + arr[n][i])
            visited[i] = 0
            
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minimum = 9999999

    find_min(0, 0)

    print(f'#{test_case} {minimum}')