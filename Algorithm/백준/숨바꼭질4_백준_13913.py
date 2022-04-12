from collections import deque

def path(x):        # 출력하는 함수
    arr = []
    temp = x
    for _ in range(visited[x] + 1):    # dist 배열에는 경로가 기록되어 있다.
        arr.append(temp)
        temp = dist[temp]
    print(' '.join(map(str, arr[::-1])))    # 출력 형식에 맞게 경로를 출력한다.


N, K = map(int, input().split())
visited = [0]*100001
dist = [0]*100001

queue = deque()
queue.append(N)

while queue:
    now = queue.popleft()
    if now == K:              # K까지 가면 출력하고 break한다.
        print(visited[now])
        path(now)
        break
    for i in (now + 1, now - 1, 2 * now):     # 세 경우에서 해야되는 일이 같아서 for문으로 처리한다.
        if 0 <= i <= 100000 and not visited[i]:
            queue.append(i)
            visited[i] = visited[now] + 1
            dist[i] = now