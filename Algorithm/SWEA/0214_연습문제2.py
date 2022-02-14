T = int(input())

for test_case in range(1, T + 1):
    numbers = list(map(int, input().split()))
    ans = 0
    for i in range(1 << len(numbers)):
        tmp = 0
        for j in range(len(numbers)):
            if i & (1 << j):
                tmp += numbers[j]
                if not tmp:
                    ans = 1
                    break
    
    print(f'#{test_case} {ans}')    