T = int(input())

for test_case in range(1, T + 1):
 
    N = float(input())
     
    ans = ''
    for i in range(-1, -14, -1):
        quot, N = divmod(N, 2 ** i)
        ans += str(int(quot))
        if N == 0:
            break
     
    if i == -13:
        ans = 'overflow'
     
    print(f'#{test_case} {ans}')