def dfs(queen, n, row):
    cnt = 0
    
    if n == row:
        return 1
    
    # 가로로 한번만 진행
    for col in range(n):
        queen[row] = col

        # for-else구문
        for x in range(row):
            # 세로로 겹치면 안됨
            if queen[x] == queen[row]: 
                break
                
            # 대각선으로 겹치면 안됨
            if abs(queen[x]-queen[row]) == (row-x):
                break
        else:
            cnt += dfs(queen, n, row+1)
            
    return cnt

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    queen = [0] * N

    ans = dfs(queen, N, 0)

    print(f'#{test_case} {ans}')