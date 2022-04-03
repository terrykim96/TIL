N = int(input())

ans = [1] * N
array = list(map(int, input().split()))

for i in range(N):
    for j in range(i):
        if array[i] < array[j] and ans[i] <= ans[j]:
            ans[i] += 1

print(max(ans))