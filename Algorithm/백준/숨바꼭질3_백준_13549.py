from collections import deque

visited = [-1] * 100001     # 방문 변수를 지정해준다.

N, K = map(int, input().split())
queue = deque()
queue.append(N)
visited[N] = 0

while queue:
    now = queue.popleft()
    if now == K:        # K까지 가면 최단거리를 출력하고 break한다.
        print(visited[K])
        break

    if 0 <= now * 2 < 100001 and visited[now * 2] == -1:  # 순간이동(now*2가 더 높은 연산 순위를 가지므로 appendleft를 사용한다.)
        queue.appendleft(now * 2)
        visited[now * 2] = visited[now]

    if 0 <= now + 1 < 100001 and visited[now + 1] == -1: # x+1이동
        queue.append(now + 1)
        visited[now + 1] = visited[now] + 1

    if 0 <= now - 1 < 100001 and visited[now - 1] == -1: # x-1이동
        queue.append(now - 1)
        visited[now - 1] = visited[now] + 1