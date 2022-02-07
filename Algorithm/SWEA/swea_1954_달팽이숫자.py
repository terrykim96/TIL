T = int(input())

direct_x = [0, 1, 0, -1]
direct_y = [1, 0, -1, 0]

for i in range(1, T+1):
    N = int(input())
    snail = [[0]*N for _ in range(N)]

    d = 0 # 방향 0: 우(0,1), 1: 하(1,0), 2: 좌(0,-1), 3: 상(-1,0)
    x = 0
    y = 0
    num = 1

    while num <= N**2:
        snail[x][y] = num # 현재칸에 값을 저장
        num += 1

        # 다음 칸 결정
        nx = x + direct_x[d]
        ny = y + direct_y[d]
        
        if 0 <= nx < N and 0 <= ny < N and not snail[nx][ny]:
            x, y = nx, ny # 현재 좌표 갱신
        
        else: # 다음 방향을 결정 (우, 하, 좌, 상의 순서)
            d = (d+1)%4 # 상에서 다시 우로 가기 위해 (리스트상 3 -> 0)
            x += direct_x[d]
            y += direct_y[d]
    
    print(f'#{i} ')
    for j in range(N):
        for k in range(N):
            print(snail[j][k], end= ' ')
        print()