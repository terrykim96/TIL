import sys

input = sys.stdin.readline

N, M = map(int, input().split())


nums = list(map(int, input().split()))
sums = [0]

tmp = 0
for i in nums:
    tmp += i
    sums.append(tmp)

for _ in range(M):
    i, j = map(int, input().split())

    print(sums[j] - sums[i - 1])