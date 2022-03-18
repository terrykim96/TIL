def check(n):
    ans[n + 1] = []
    dx = [0, 0, 1, -1]  # 동 서 남 북
    dy = [1, -1, 0, 0]
    tmp_list = ans[n]
    for i in range(len(tmp_list)):
        for j in range(4):
            if j == 0:
                if board[tmp_list[i][0]][tmp_list[i][1]] in [1, 3, 4, 5] and 0 <= tmp_list[i][0] + dx[j] < N and 0 <= tmp_list[i][1] + dy[j] < M and [tmp_list[i][0] + dx[j], tmp_list[i][1] + dy[j]] not in visited and board[tmp_list[i][0] + dx[j]][tmp_list[i][1] + dy[j]] in [1, 3, 6, 7]:
                    visited.append([tmp_list[i][0] + dx[j], tmp_list[i][1] + dy[j]])
                    ans[n + 1].append([tmp_list[i][0] + dx[j], tmp_list[i][1] + dy[j]])
            elif j == 1:
                if board[tmp_list[i][0]][tmp_list[i][1]] in [1, 3, 6, 7] and 0 <= tmp_list[i][0] + dx[j] < N and 0 <= tmp_list[i][1] + dy[j] < M and [tmp_list[i][0] + dx[j], tmp_list[i][1] + dy[j]] not in visited and board[tmp_list[i][0] + dx[j]][tmp_list[i][1] + dy[j]] in [1, 3, 4, 5]:
                    visited.append([tmp_list[i][0] + dx[j], tmp_list[i][1] + dy[j]])
                    ans[n + 1].append([tmp_list[i][0] + dx[j], tmp_list[i][1] + dy[j]])
            elif j == 2:
                if board[tmp_list[i][0]][tmp_list[i][1]] in [1, 2, 5, 6] and 0 <= tmp_list[i][0] + dx[j] < N and 0 <= tmp_list[i][1] + dy[j] < M and [tmp_list[i][0] + dx[j], tmp_list[i][1] + dy[j]] not in visited and board[tmp_list[i][0] + dx[j]][tmp_list[i][1] + dy[j]] in [1, 2, 4, 7]:
                    visited.append([tmp_list[i][0] + dx[j], tmp_list[i][1] + dy[j]])
                    ans[n + 1].append([tmp_list[i][0] + dx[j], tmp_list[i][1] + dy[j]])
            else:
                if board[tmp_list[i][0]][tmp_list[i][1]] in [1, 2, 4, 7] and 0 <= tmp_list[i][0] + dx[j] < N and 0 <= tmp_list[i][1] + dy[j] < M and [tmp_list[i][0] + dx[j], tmp_list[i][1] + dy[j]] not in visited and board[tmp_list[i][0] + dx[j]][tmp_list[i][1] + dy[j]] in [1, 2, 5, 6]:
                    visited.append([tmp_list[i][0] + dx[j], tmp_list[i][1] + dy[j]])
                    ans[n + 1].append([tmp_list[i][0] + dx[j], tmp_list[i][1] + dy[j]])
 
 
T = int(input())
 
for test_case in range(1, T + 1):
    '''
    N = 세로길이, M = 가로길이
    (R, C) = 맨홀 뚜껑 위치
    L = 탈출 후 소요된 시간
    '''
    N, M, R, C, L = list(map(int, input().split()))
    board = [list(map(int, input().split())) for _ in range(N)]
 
    ans = {
        1: [[R, C]]
    }
    visited = [[R, C]]
 
    for i in range(1, L):
        check(i)
 
    result = 0
    for i in range(1, L + 1):
        result += len(ans[i])

    print(f'#{test_case} {result}')