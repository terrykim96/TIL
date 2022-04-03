N = int(input())

# 길이가 1 늘어나는 경우 맨 뒷자리 수의 경우의 수는 그 항목의 경우의 수 전의 경우의 수 + 그 항목 전의 길이의 경우의 수이다.
dp = [1] * 10

for i in range(1, N):
    for j in range(1, 10):
        dp[j] += dp[j - 1]

print(sum(dp) % 10007)