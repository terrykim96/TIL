T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    arrive_time = list(map(int, input().split()))
    arrive_time.sort()

    ans = "Possible"
    for i in range(N):      # x초까지 만들어진 붕어 개수: (x // M) * K
        bread = (arrive_time[i] // M) * K - (i+1)
        if bread < 0:
            ans = "Impossible"
            break

    print(f'#{test_case} {ans}')