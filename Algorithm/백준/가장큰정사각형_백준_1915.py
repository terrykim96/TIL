import sys

input = sys.stdin.readline

n, m = map(int, input().split())

matrix = []

# 정사각형 변 길이 저장할 dp 행렬을 생성한다.
dp = [[0] * m for _ in range(n)]

for _ in range(n):
    matrix.append(list(map(int, list(input().rstrip()))))

ans = 0
for i in range(n):
    for j in range(m):              # 행렬 전체를 돌면서 각 지점이 정사각형의 우하단 꼭지점일때의 최대 변 길이를 저장한다.

        if i == 0 or j == 0:        # 둘다 0 일때는 변 길이가 1 아니면 0
            dp[i][j] = matrix[i][j]

        elif matrix[i][j] == 0:     # 0이면 정사각형을 못만든다.
            dp[i][j] = 0

        else:                       #  왼쪽, 대각선, 위쪽 중 가장 작은 변에 +1을 한 것이 변의 최대 길이이다.
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        ans = max(dp[i][j], ans)

print(ans * ans)