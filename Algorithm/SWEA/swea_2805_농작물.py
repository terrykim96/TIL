T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    farm = []
    for i in range(N):
        farm.append(list(map(int, input())))

    ans = 0
    start = end = N // 2        # 마름모의 시작점과 끝점을 지정한다. 중간부터 퍼져나가는 방식이다.
    for i in range(N):          # 각 줄에 대해 마름모의 시작점부터 끝점까지 더해준다.
        for j in range(start, end + 1):
            ans += farm[i][j]
        if i < N //2:           # 마름모의 중간까지는 시작점과 끝점이 점점 멀어지고
            start -= 1
            end += 1
        else:                   # 중간 이후로는 점점 가까워진다.
            start += 1
            end -= 1
    
    print(f'#{test_case} {ans}')