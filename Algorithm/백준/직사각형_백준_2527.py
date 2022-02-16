for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    
    # 왼쪽 벽 중 x좌표가 큰 변과 오른쪽 벽 중 x좌표가 작은 변의 차를 x_df,
    # 아래쪽 벽 중 y좌표가 큰 변과 위쪽 벽 중 y좌표가 작은 변의 차를 y_df로 설정
    left = max(x1, x2)
    right = min(p1, p2)
    bottom = max(y1, y2)
    top = min(q1, q2)

    x_df = left - right
    y_df = bottom - top

    # x_df와 y_df가 모두 0보다 작으면 a, 둘 중 하나라도 0보다 크면 d, 둘다 0이면 c, 하나만 0이면 b이다.
    if x_df < 0 and y_df < 0:
        print('a')
    elif x_df > 0 or y_df > 0:
        print('d')
    elif x_df == 0 and y_df == 0:
        print('c')
    else:
        print('b')