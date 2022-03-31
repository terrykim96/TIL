def bfs(x, max_val):
    global ans
    #값이 계산한 이전값보다 작다면 리턴
    if max_val <= ans: return
    #위에서 걸러지므로 여기까지 왔다면 그냥 값을 넣는다.
    if x >= N:
        ans = max_val
        return
    #조합을 구해서 bfs하기
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            bfs(x + 1, max_val * (numbers[x][i] / 100))
            visited[i] = 0
 
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    #람다식을 이용하여 넣을때부터 100으로 나누어 사용
    numbers = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    ans = 0

    bfs(0, 1)
    answer = ans * 100

    #6자리수로 제한하여 출력

    print(f'#{test_case} {"%.6f" %answer}')