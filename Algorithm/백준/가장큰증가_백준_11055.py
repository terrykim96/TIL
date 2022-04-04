N = int(input())
array = list(map(int, input().split()))

ans = [0] * N       # ans[i]는 array[i]까지의 증가 부분 수열의 합이다.
ans[0] = array[0]

for i in range(1, N):
    for j in range(i):
        if array[j] < array[i]:
            ans[i] = max(ans[i], ans[j] + array[i])
        else:
            ans[i] = max(ans[i], array[i])

print(max(ans))