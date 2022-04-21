N = int(input())
time = list(map(int, input().split()))

ans = 0
time.sort() # 걸리는 시간을 오름차순으로 정렬해준다.(오름차순으로 하면 가장 빠름)

for i in range(N):
    ans += sum(time[: (i + 1)])  # 각 사람별로(i) 시간의 합을 계산해준다.
print(ans)