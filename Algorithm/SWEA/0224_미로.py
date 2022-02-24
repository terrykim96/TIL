T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, input())))
    direct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    ans = 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                x = j
                y = i
            break
        
    stk = [(y, x)]
    while stk:
        tmp_lst = []
        y, x = stk.pop()
        maze[y][x] = 1
        
        for dy, dx in direct:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            elif maze[ny][nx] == 2:
                ans = 1
                break
            elif not maze[ny][nx]:
                stk.append((ny, nx))
        else:
            continue

    print(f'#{test_case} {ans}')