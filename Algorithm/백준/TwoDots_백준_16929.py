N, M=map(int,input().split())

arr=[list(map(str,input()))for _ in range(N)]
visited = [[0] * M for _ in range(N)]

direction_i = [0, 0, 1, -1]
direction_j = [1, -1, 0, 0]
 
def dfs(i, j, si, sj, color):    # dfs로 찾아준다.

    if visited[i][j] == 1:      # 한바퀴를 돌아서 방문했던 점으로 돌아오면 싸이클이 존재하는 것이기 때문에 바로 True를 반환한다.
        return True

    visited[i][j] = 1
 
    for d in range(4):
        ni = i + direction_i[d]
        nj = j + direction_j[d]

        if ni != si or nj != sj:    # 바로 전 점을 방문하지 않도록 하기 위해 si, sj 변수를 추가해줬다.
            if ni >= 0 and ni < N and nj >= 0 and nj < M:
                if arr[ni][nj] == color :   # 색이 같으면 재귀로 dfs 구현한다.
                    if dfs(ni, nj, i, j, color):
                        return True
    return False

ans = 'No'

for i in range(N):
    for j in range(M):
        if visited[i][j]:
            continue

        if dfs(i, j, 0, 0, arr[i][j]):
            ans = 'Yes'
            break
    if ans == 'Yes':
        break

print(ans)