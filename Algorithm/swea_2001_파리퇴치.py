T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    flies = []
    died_flies = 0
    for _ in range(N):
        flies.append(list(map(int, input().split())))
    
    # M x M 크기의 파리채를 catch에 저장한 후 죽은 파리 수가 제일 큰 died_flies를 출력한다.
    for j in range(N - M + 1):
        for k in range(N - M + 1):
            catch = []
            for l in range(M):
                catch.append(flies[j + l][k : k + M])
            print(catch)
            if died_flies <= sum(sum(catch, [])):
                died_flies = sum(sum(catch, []))
    print(f'#{i} {died_flies}')