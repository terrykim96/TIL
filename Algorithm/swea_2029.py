T = int(input())

for i in range(T):
    numbers = list(map(int, input().split()))

    print(f'#{i+1} {numbers[0] // numbers[1]} {numbers[0] % numbers[1]}')