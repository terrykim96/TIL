from collections import deque
 
def bfs(N, M):
    queue = deque()
    queue.append((N, 0))
    check = {}
    while queue:
        item, cnt = queue.popleft()
        if check.get(item, 0):
            continue

        check[item] = 1

        if item == M:
            return cnt
        cnt += 1
        if 0 < item+1 <= 1000000:
            queue.append((item+1, cnt))
        if 0 < item-1 <= 1000000:
            queue.append((item-1, cnt))
        if 0 < item*2 <= 1000000:
            queue.append((item*2, cnt))
        if 0 < item-10 <= 1000000:
            queue.append((item-10, cnt))

T = int(input()) 
for test_case in range(1, T + 1):
    N,M = map(int, input().split())

    print(f'#{test_case} {bfs(N,M)}')