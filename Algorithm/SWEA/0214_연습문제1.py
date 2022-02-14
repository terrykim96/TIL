T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for test_case in range(1, T + 1):
    N = int(input())
    numbers = []
    ans = 0

    for i in range(N):
        numbers.append(list(map(int, input().split())))
    
    for k in range(N):
        for m in range(N):
            for n in range(4):
                x = m + dx[n]
                y = k + dy[n]
                if 0 <= x < N and 0<= y < N:
                    ans += abs(numbers[k][m] - numbers[y][x])
    print(f'#{test_case} {ans}')
            