T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    numbers = list(range(1, 13))
    cnt = 0

    for i in range(1 << len(numbers)):
        lst = []
        for j in range(len(numbers)):
            if i & (1 << j):
                lst.append(numbers[j])
        if len(lst) == N:
            tmp = 0
            for num in lst:
                tmp += num
            if tmp == K:
                cnt += 1
    print(f'#{test_case} {cnt}')