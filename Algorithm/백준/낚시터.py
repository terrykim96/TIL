from collections import deque

def bfs(gate):
    global cnt

    queue = deque([gate[0]])
    visited[x] = 1
    
    while queue:
        x = queue.popleft()

        for i in range(gate[1]):
            pass


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    gate1 = list(map(int, input().split()))
    gate2 = list(map(int, input().split()))
    gate3 = list(map(int, input().split()))
    visited = [0] * (N + 1)
    ans = 10e6
    cnt = 0

    dfs(gate1[0], gate1)

    print(cnt)