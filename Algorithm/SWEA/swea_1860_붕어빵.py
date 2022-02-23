T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort()

    ans = "Possible"
    for i in range(N):      # x초까지 만들어진 붕어 개수: (x // M) * K
        bread = (lst[i] // M) * K - (i+1)
        if bread < 0:
            ans = "Impossible"
            break

    print(f'#{test_case} {ans}')