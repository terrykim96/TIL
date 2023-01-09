import sys

input = sys.stdin.readline

n = int(input())
expected = []

for _ in range(n):
    expected.append(int(input()))

expected.sort()     # 정렬

ans = sum([abs(i - j) for i, j in zip(expected, list(range(1, n + 1)))])

result = 0
for i in range(1, n + 1):
    result += abs(i - expected[i - 1])      # 예상 등수와 실제 등수 차이를 비교한다.

print(result)