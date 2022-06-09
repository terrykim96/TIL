N, M = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 1
cnt = 0

while right <= N and left <= right:
    tmp = sum(arr[left : right])

    if tmp == M:
        cnt += 1
        right += 1
    
    elif tmp < M:
        right += 1
    
    else:
        left += 1

print(cnt)