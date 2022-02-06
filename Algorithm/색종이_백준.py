N = int(input())
area = [[0]*1001 for _ in range(1001)]  # 전체 좌표평면을 생성한다.

for paper in range(N):                                  # 색종이 순서대로
    x1, y1, width, height = map(int, input().split())   # 각 좌표를 저장한다.

    x2 = x1 + width - 1                 
    y2 = y1 + height -1

    for i in range(x1, x2 + 1):         # 저장된 좌표에 대해
        for j in range(y1, y2 + 1):     # 좌표평면에서 해당하는 좌표 범위 내의 숫자를 표시 (색종이 번호로)
            area[i][j] = paper + 1      # 나중에 나오는 색종이로 덮어쓰기 가능하게

for i in range(N):                      # 좌표평면에서 각 색종이에 해당하는 번호 count해서 출력
    cnt  = 0
    for j in area:
        cnt += j.count(i + 1)
    print(cnt)