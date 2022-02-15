dx = [-1, 0, 0]
dy = [0, 1, -1]

T = int(input())

for test_case in range(1, T + 1):
    # 양 끝에 벽을 세워주기 위해 0 컬럼 추가
    ladder = [[0] + list(map(int, input().split())) + [0] for _ in range(100)]

    # c: 도착점 column idx 구하기
    for j in range(102):
        if ladder[99][j] == 2:
            y = j

    # 방향 위로 초기화
    d = 0  # 0: 위, 1: 오, 2: 왼
    x = 99
    while True:
        # 반복문 계속 돌리다가 row 인덱스가 0 이 되면 끝내고 리턴
        if x == 0:
            break

        # 왼쪽에 1이 있으면 왼쪽으로 계속 가다가 0 나오면 반복문 종료
        if ladder[x][y - 1]:
            d = 2
            while True:
                x += dx[d]
                y += dy[d]
                if ladder[x][y - 1] == 0:
                    break

        # 오른쪽에 1이 있으면 오른쪽으로 계속 가다가 0 나오면 반복문 종료
        elif ladder[x][y + 1]:
            d = 1
            while True:
                x += dx[d]
                y += dy[d]
                if ladder[x][y + 1] == 0:
                    break

        d = 0
        x += dx[d]
        y += dy[d]

    print('#{test_case}' , y-1)