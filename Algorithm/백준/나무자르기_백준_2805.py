N, M = map(int, input().split())
trees = list(map(int, input().split()))

start, end = 1, max(trees)

while start <= end:     # 이분탐색으로 찾아준다.
    mid = (start + end) // 2

    tree_len = 0

    for tree in trees:
        if tree >= mid:
            tree_len += tree - mid
    
    if tree_len >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)