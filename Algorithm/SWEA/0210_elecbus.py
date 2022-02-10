T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    char_list = list(map(int, input().split()))
    cnt = 0
    i = 0
    while True:
        i += K

        if i >= N:
            break

        for j in range(i, i - K, -1):
            if j in char_list:
                cnt += 1
                i = j
                break
        else:
            cnt = 0
            break
        

    print(f'#{test_case} {cnt}')