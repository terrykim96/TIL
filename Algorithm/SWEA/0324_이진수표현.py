T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    ans = 'ON'

    for i in range(N):
        # 1이 아닌 것이 있다면 off
        if not M & (1 << i):
            ans = 'OFF'        
    
    print(f'#{test_case} {ans}')