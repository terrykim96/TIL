area = [[0]*100 for _ in range(100)]    # 전체 좌표평면을 만든다

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())  # 각 좌표를 저장


    for i in range(x1, x2):                 # 저장된 좌표에 대해
        for j in range(y1, y2):
            area[i][j] += 1                 # 좌표평면에서 해당하는 좌표 범위 내의 숫자를 표시 (+1로)

width = 0
for i in range(len(area)):              # 표시가 끝나면 칠해진 전체 범위를 탐색하며 0이 아니면 넓이를 추가
    for j in range(len(area)):
        if area[i][j] > 0:
            width += 1
print(width)