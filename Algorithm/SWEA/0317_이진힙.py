def heap():
    for i in range(1, N + 1):
        while i != 1:
            p = i // 2
            if board[i] < board[p]:
                board[i], board[p] = board[p], board[i]
            i //= 2
             
T = int(input()) 
for test_case in range(1, T + 1):
    N = int(input())
    board = [0] + [int(x) for x in input().split()]
    heap()
     
    ans = 0
    while N > 1:
        N //= 2
        ans += board[N]
 
    print(f'#{test_case} {ans}')