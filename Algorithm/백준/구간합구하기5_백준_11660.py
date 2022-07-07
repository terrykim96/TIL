import sys

input = sys.stdin.readline

N, M = map(int, input().split())

numbers = [[0] * (N + 1)]

for _ in range(N):
    nums = [0] + [int(x) for x in input().split()]
    numbers.append(nums)


for i in range(1, N + 1):
    for j in range(1, N):
        numbers[i][j + 1] += numbers[i][j]

for j in range(1, N + 1):
    for i in range(1, N):
        numbers[i + 1][j] += numbers[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    # (x1, y1)에서 (x2, y2)까지의 합 = p[x2][y2] - p[x1 - 1][y2] - p[x2][y1 - 1] + p[x1 - 1][y1 - 1]
    print(numbers[x2][y2] - numbers[x1 - 1][y2] - numbers[x2][y1 - 1] + numbers[x1 - 1][y1 - 1])