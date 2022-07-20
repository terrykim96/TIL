import sys
from collections import deque

input = sys.stdin.readline

dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
hx, hy = [-2, -2, -1, 1, 2, 2, -1, 1], [-1, 1, -2, -2, -1, 1, 2, 2]     # 말처럼 움직이는 방향


def bfs():
    q = deque()
    q.append((0, 0, K, 0))  # (맨 왼쪽 위, 인덱스, 말처럼 움직일 기회가 몇번 남았는지, 이동 횟수) 형태로 큐에 넣는다.

    visited = [[[0] * (K + 1) for _ in range(W)] for _ in range(H)]  # 세로 좌표, 가로 좌표, 남은 점프 횟수
    visited[0][0][K] = 1

    while q:
        i, j, k, cnt = q.popleft()

        if i == (H - 1) and j == (W - 1):       # 목적지 도착했으면 cnt를 return한다.
            return cnt

        if k > 0:
            for m in range(8):                  # 말처럼 이동 가능하면 말처럼 이동한다.
                ni, nj = i + hx[m], j + hy[m]

                if 0 <= ni < H and 0 <= nj < W and not arr[ni][nj] and not visited[ni][nj][k - 1]:  # 지도 범위내에 있고 방문하지 않았고 목적지가 장애물이 아니라면 이동한다.
                    visited[ni][nj][k - 1] = 1

                    q.append((ni, nj, k - 1, cnt + 1))      # 말처럼 이동 가능한 횟수를 줄이고, 이동 횟수를 늘리고 다음 칸으로 이동한다.

        for m in range(4):                      # 말처럼 이동 불가능하면 사방으로만 이동한다.
            ni, nj = i + dx[m], j + dy[m]

            if 0 <= ni < H and 0 <= nj < W and not arr[ni][nj] and not visited[ni][nj][k]:    # 지도 범위내에 있고 방문하지 않았고 목적지가 장애물이 아니라면 이동한다.
                visited[ni][nj][k] = 1

                q.append((ni, nj, k, cnt + 1))


    return -1       # 도착점에 도착할 수 없으면 -1을 반환한다.


K = int(input())
W, H = map(int, input().split())
arr = tuple(tuple(map(int, input().split())) for _ in range(H))
print(bfs())