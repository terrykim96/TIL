N = int(input())
stair = [0] * 301
dp = [0] * 301

for i in range(N):
    stair[i] = int(input())

dp[0] = stair[0]                # 첫번째에는 첫번째 점수가 들어간다.
dp[1] = stair[0] + stair[1]     # 두번쨰에는 첫번째 점수와 두번째 점수를 합한 값을 넣어준다.
dp[2] = max(stair[1] + stair[2], stair[0] + stair[2])   # 첫 계단을 밟고 두 계단을 올랐을 떄의 합 / 두번째 계단을 밟고 한 계단을 올랐을 때의 합 중에 큰 값을 넣어준다.

for i in range(3, N):
    dp[i] = max(dp[i - 3] + stair[i - 1] + stair[i], dp[i - 2] + stair[i])  # 마지막 계단의 전 계단을 밟은 경우와 밟지 않은 경우 중 큰 값을 넣어준다.

print(dp[N - 1])