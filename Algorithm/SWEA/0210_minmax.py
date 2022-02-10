T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    minimum = 10e8
    maximum = 0

    for num in numbers:
        if minimum > num:
            minimum = num
        if maximum < num:
            maximum = num
    
    print(f'#{test_case} {maximum - minimum}')