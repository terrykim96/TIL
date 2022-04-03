N = int(input())
wine = [0] * 10000

# 전전(n-2)까지의 최대 양 + 현재 양과
# 전전전(n-3)까지의 최대 양 + 전(n-1)번째 양 + 현재 양 중에 큰 값을 ans에 저장한다.

for i in range(N):
    wine[i] = int(input())

ans = [0] * 10000
ans[0] = wine[0]   # d[i]는 i번째 포도주까지 최대로 마신 포도주의 양이다.
ans[1] = wine[0] + wine[1]
ans[2] = max(wine[2] + wine[0], wine[2] + wine[1], ans[1])

for i in range(3, N):
    ans[i] = max(wine[i] + ans[i-2], wine[i] + wine[i-1] + ans[i-3], ans[i-1])

print(max(ans))