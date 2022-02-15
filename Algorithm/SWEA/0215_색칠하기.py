T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = [[0]*10 for _ in range(10)]
    
    for i in range(N):
        x1, y1, x2, y2, color = map(int, input().split())

        if color == 1:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if lst[x][y] == 0:
                        lst[x][y] = 1
                    elif lst[x][y] == 2:
                        lst[x][y] = 3
        
        if color == 2:
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    if lst[x][y] == 0:
                        lst[x][y] = 2
                    elif lst[x][y] == 1:
                        lst[x][y] = 3
    cnt = 0
    for i in range(10):
        for j in range(10):
            if lst[i][j] == 3:
                cnt += 1
                
    print(f'#{test_case} {cnt}')