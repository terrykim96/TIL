N = int(input())

ans = [1] * N       # 가장 작은 길이는 1이므로 1부터 시작
array = list(map(int, input().split()))

for i in range(N):
    for j in range(i):
        if array[i] < array[j] and ans[i] <= ans[j]:
            ans[i] += 1

print(max(ans))