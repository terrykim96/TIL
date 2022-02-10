T = 10
for test_case in range(1, T + 1):
    N = int(input())
    box = list(map(int, input().split()))
    height = [0] * 101
    minimum = 1000
    maximum = 0
    
    for i in range(100):
        height[box[i]] += 1
        if maximum < box[i]:
            maximum = box[i]
        if minimum > box[i]:
            minimum = box[i]

    while N > 0 and minimum < (maximum - 1):
        height[minimum + 1] += 1
        height[minimum] -= 1

        height[maximum] -= 1
        height[maximum - 1] += 1

        if height[minimum] == 0:
            minimum += 1
        if height[maximum] == 0:
            maximum -= 1
        
        N -= 1

    print(f'#{test_case} {maximum - minimum}')