n = int(input())

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


dragon = [[0] * 101 for _ in range(101)]    # 드래곤 커브들이 모일 배열 1이면 드래곤 커브의 일부이다.

for _ in range(n):
    x, y, d, g = map(int, input().split())  # x, y : 드래곤 커브 시작점, d : 시작 방향, g : 세대
    
    dragon[x][y] = 1

    move = [d]
    
    for _ in range(g):                      # g 세대 만큼 반복한다.
        tmp = []
        for i in range(len(move)):
            tmp.append((move[-i - 1] + 1) % 4)
        move.extend(tmp)

    
    for i in move:                          # 드래곤 커브에 해당하는 좌표 dragon에 추가한다.
        nx = x + dx[i]
        ny = y + dy[i]
        dragon[nx][ny] = 1
        x, y = nx, ny


ans = 0
for i in range(100):                        # 모든 꼭짓점이 드래곤 커브의 일부인 정사각형 개수 구한다.
    for j in range(100):
        if dragon[i][j] and dragon[i + 1][j] and dragon[i][j + 1] and dragon[i + 1][j + 1]:
            ans += 1

print(ans)