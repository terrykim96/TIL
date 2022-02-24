T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int,input().split())
    numbers = list(map(int, input().split()))
    cnt = 0
    lst = []

    for i in range(1 << len(numbers)):
        tmp = []
        for j in range(len(numbers)):
            if i & (1 << j):
                tmp.append(numbers[j])
        lst.append(tmp)
        
    for num in lst:
        sums = 0
        for number in num:
            sums += number
        if sums == K:
            cnt += 1

    print(f'#{test_case} {cnt}')