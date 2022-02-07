T = int(input())

for i in range(1, T+1):
    matrix_a = []
    matrix_size = int(input())
    
    for j in range(matrix_size):
        matrix_a.append(list(map(int, input().split())))
    
    turn_90 = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
    turn_180 = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]
    turn_270 = [[0 for _ in range(matrix_size)] for _ in range(matrix_size)]

    # 90도 회전
    for j in range(matrix_size):
        for k in range(matrix_size):
            turn_90[j][k] = matrix_a[matrix_size - 1 - k][j]
    
    # 90도 회전을 90도 회전하면 180도 회전한 것
    for j in range(matrix_size):
        for k in range(matrix_size):
            turn_180[j][k] = turn_90[matrix_size - 1 - k][j]

    # 180도 회전을 90도 회전하면 270도 회전한 것
    for j in range(matrix_size):
        for k in range(matrix_size):
            turn_270[j][k] = turn_180[matrix_size - 1 - k][j]
    
    print(f'#{i} ')
    for j in range(matrix_size):
        for a in range(matrix_size):
            print(turn_90[j][a], end= '')
        print(end= ' ')
        for b in range(matrix_size):
            print(turn_180[j][b], end= '')
        print(end= ' ')
        for c in range(matrix_size):
            print(turn_270[j][c], end= '')
        print()