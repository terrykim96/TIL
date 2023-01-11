N = int(input())

ans = [1] * N       # 가장 작은 길이는 1이므로 1부터 시작
numbers = list(map(int, input().split()))

for i in range(N):
    for j in range(i):
        if numbers[i] < numbers[j] and ans[i] <= ans[j]:    # 감소 수열이면서 길이가 더 짧지 않으면 길이에 1을 추가해준다.
            ans[i] += 1

print(max(ans))     # 가장 긴 길이를 구한다.