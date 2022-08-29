def find(board):
    fix = 0
    cores = []

    for i in range(N):
        for j in range(N):
            if board[i][j]:
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    fix += 1
                else:
                    cores.append((i, j))

    return fix, cores

direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]

def cancel(i, j, dir, cnt):
    di, dj = direction[dir]

    for _ in range(cnt):
        board[i + di][j + dj] = 0
        i += di
        j += dj

def install(i, j, dir):
    si = i
    sj = j
    di, dj = direction[dir]
    cnt = 0

    while 0 <= i + di < N and 0 <= j + dj < N:
        i += di
        j += dj

        if board[i][j]:
            break

        board[i][j] = 1
        cnt += 1
        
    else:
        return cnt
    cancel(si, sj, dir, cnt)
    return 0

def dfs(now, last, code):
    global max_cores, min_code

    if max_cores < len(now):
        max_cores = len(now)
        min_code = 12*12 + 1

    if max_cores == len(now) and min_code > code:
        min_code = code

    for i in range(last, len(cores)):
        for dir in range(4):
            cnt = install(*cores[i], dir)

            if not cnt:
                continue
            next = now[:]
            next.append(i)

            dfs(next, i + 1, code + cnt)
            cancel(*cores[i], dir, cnt)


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    fix, cores = find(board)

    max_cores = -1
    min_code = 12*12 + 1

    dfs([], 0, 0)

    print(f'#{test_case} {min_code}')