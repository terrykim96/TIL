N = int(input())
arr = []
arr = list(map(int, input().split()))
dp = [ [0] * (N + 2) for _ in range(2) ]
dp[0][0] = arr[0]       # 제거를 안하는 경우
dp[1][0] = 0            # 제거를 하는 경우
ans = arr[0]

for i in range(1, N):
    dp[0][i] = max(dp[0][i-1] + arr[i], arr[i])           # 기존 숫자 이어서 하던지, 현재 숫자만 한다.
    dp[1][i] = max(dp[0][i-1], dp[1][i-1] + arr[i])       # 현재 숫자를 제거하고, 기존 숫자제거 + 현재 숫자
    ans = max(dp[0][i],dp[1][i], ans)

print(ans)