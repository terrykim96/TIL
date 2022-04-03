T = int(input())

for _ in range(T):
    s = []
    N = int(input())

    for _ in range(2):
        s.append(list(map(int, input().split())))

    for i in range(1, N):
        if i == 1:  # 1번 인덱스에는 왼쪽 대각선의 숫자를 더할 수 있다.
            s[0][i] += s[1][i - 1]
            s[1][i] += s[0][i - 1]

        else: # 2번째 인덱스부터는 이때까지 최댓값을 더한 숫자를 저장하고 있는 왼쪽 대각선의 숫자 또는 그 왼쪽 숫자를 더할 수 있다. 이 둘중에 큰 값을 더해주면 된다.
            s[0][i] += max(s[1][i - 1], s[1][i - 2])
            s[1][i] += max(s[0][i - 1], s[0][i - 2])

    print(max(s[0][N - 1], s[1][N - 1]))