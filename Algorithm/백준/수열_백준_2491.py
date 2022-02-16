N = int(input())
numbers = list(map(int, input().split()))
ans = 1
cnt1 = 1
cnt2 = 1

# 다음 숫자와 비교해서 커지거나 같으면 cnt1에 1을 더하고 가장 큰 cnt1를 ans에 저장
for i in range(N - 1):
    if numbers[i] <= numbers[i + 1]:
        cnt1 += 1
    else:
        cnt1 = 1

    if ans < cnt1:
        ans = cnt1

# 다음 숫자와 비교해서 작아지거나 같으면 cnt2에 1을 더하고 가장 큰 cnt2를 ans와 비교해서 더 크면 저장
for i in range(N - 1):
    if numbers[i] >= numbers[i + 1]:
        cnt2 += 1
    else:
        cnt2 = 1   

    if ans < cnt2:
        ans = cnt2

print(ans)