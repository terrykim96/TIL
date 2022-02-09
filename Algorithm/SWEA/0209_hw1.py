T = int(input())

for i in range(1, T+1):
    
    num_length = int(input())
    numbers = list(map(int, input().split()))

    for j in range(num_length-1, 0, -1):
        for k in range(0, j):
            if numbers[k] > numbers[k+1]:
                numbers[k], numbers[k+1] = numbers[k+1], numbers[k]
    
    print(f'#{i}', end= ' ')
    print(*numbers)