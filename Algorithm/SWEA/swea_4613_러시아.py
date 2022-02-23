T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    ans = N * M     # 최대 N * M번 바꿔야 하므로 최솟값인 ans를 N * M으로 설정
    w_cnt = 0

    # 반복문으로 모든 경우의 수를 계산해서 최솟값을 찾는다.
    for w in range(N - 2):  # 흰색 먼저
        for i in range(M):
            if flag[w][i] != 'W':
                w_cnt += 1

        b_cnt = 0
        for b in range(w + 1, N - 1):   # 파란색
            for j in range(M):
                if flag[b][j] != 'B':
                    b_cnt += 1
            
            r_cnt = 0
            for r in range(b + 1, N):   # 빨간색
                for k in range(M):
                    if flag[r][k] != 'R':
                        r_cnt += 1
            
            cnt = w_cnt + b_cnt + r_cnt
            if ans > cnt:
                ans = cnt
    
    print(f'#{test_case} {ans}')