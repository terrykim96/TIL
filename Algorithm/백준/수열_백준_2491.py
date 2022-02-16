N = int(input())
numbers = list(map(int, input().split()))
ans_1 = 0
ans_2 = 0

for i in range(N):
    cnt = 1
    num = numbers[i]
    for j in range(i + 1, N):
        if num <= numbers[j]:
            cnt += 1
            num = numbers[j]
        else:
            break
    if ans_1 < cnt:
        ans_1 = cnt

for i in range(N):
    cnt = 1
    num = numbers[i]
    for j in range(i + 1, N):
        if num >= numbers[j]:
            cnt += 1
            num = numbers[j]
        else:
            break
    if ans_2 < cnt:
        ans_2 = cnt
        
print(max(ans_1, ans_2))