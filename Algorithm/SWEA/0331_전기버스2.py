def dfs(x, depth):
    global ans
    if answer < depth: return
    if x >= N:
        answer = depth
        return
    cnt = station[x]
    for i in range(cnt, 0, -1):
        dfs(x+i, depth + 1)
 
 
for test_case in range(int(input())):
    ans = 10e6
    station = list(map(int, input().split()))
    #0부터 시작하니까 -1
    N = station.pop(0) - 1
    #처음 충전은 안치니까 -1로 시작해서 보정해주기
    dfs(0, -1)
    print(f'#{test_case} {ans}')