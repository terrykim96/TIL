def paste(N):
    if N == 20:
        return 3
    elif N == 10:
        return 1
    else:
        return paste(N - 10) + 2 * paste(N - 20)

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    ans = paste(N)

    print(f'#{test_case} {ans}')