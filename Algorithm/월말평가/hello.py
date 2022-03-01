T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maps = []
    for _ in range(N):
        maps.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            if maps[i][j] == 2:
                si = i
                sj = j
                break

    for j in range(sj, N):
        if maps[si][j] == 0:
            maps[si][j] = 3
        elif maps[si][j] == 1:
            break

    for j in range(sj, -1, -1):
        if maps[si][j] == 0:
            maps[si][j] = 3
        elif maps[si][j] == 1:
            break

    for i in range(si, N):
        if maps[i][sj] == 0:
            maps[i][sj] = 3
        elif maps[i][sj] == 1:
            break
    for i in range(si, -1, -1):
        if maps[i][sj] == 0:
            maps[i][sj] = 3
        elif maps[i][sj] == 1:
            break

    ans = 0

    for i in range(N):
        ans += maps[i].count(0)

    print(f'#{test_case} {ans}')