def solution(m, n, board): 
    ans = 0
    for i in range(len(board)):
       board[i] = list(board[i])

    while True:
        remove = [[0]*n for _ in range(m)]  # 같은 모양의 2X2 블록을 찾으면 remove 배열에 1로 표시한다.
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] != 0 and board[i][j] == board[i][j + 1] and board[i][j] == board[i + 1][j] and board[i][j] == board[i + 1][j + 1]:
                    remove[i][j], remove[i][j + 1], remove[i + 1][j], remove[i + 1][j + 1] = 1, 1, 1, 1
        
        cnt = 0
        for i in range(m):  # 지워진 블록 개수를 센다
            cnt += sum(remove[i])
        ans += cnt

        if cnt == 0:        # 지워진 블록이 없을 경우 break
            break

        for i in range(m - 1, -1, -1):  # 지워진 블록을 위의 블록으로 채운다.
            for j in range(n):
                if remove[i][j] == 1:
                    ni = i - 1
                    while ni >= 0 and remove[ni][j] == 1:
                        ni -= 1
                    if ni < 0:
                        board[i][j] = 0
                    else:
                        board[i][j] = board[ni][j]
                        remove[ni][j] = 1
    
    return ans