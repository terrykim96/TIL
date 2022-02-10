T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    tmp = 0

    for num in numbers[:M]:
        tmp += num
        
    minimum = tmp
    maximum = tmp

    for i in range(M, N):           
        tmp += numbers[i]
        tmp -= numbers[i - M]

        if minimum > tmp:
            minimum = tmp
        if maximum < tmp:
            maximum = tmp

    print(f'#{test_case} {maximum - minimum}')