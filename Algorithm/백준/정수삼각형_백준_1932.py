N = int(input())

t_list = []

for _ in range(N):
    t_list.append(list(map(int, input().split())))


for i in range(1, N):   # 삼각형의 꼭대기부터 내려오면서 최대 값을 저장한다.
    for j in range(i + 1):
        if j == 0:
            t_list[i][j] = t_list[i][j] + t_list[i-1][j]
        elif i == j:
            t_list[i][j] = t_list[i][j] + t_list[i-1][j-1]
        else:           # 삼각형의 가장 밑에는 해당 값까지 오기 위한 최대 값이 저장되고, max를 이용해 가장 큰 값을 고른다.
            t_list[i][j] = max(t_list[i][j]+t_list[i-1][j],
                               t_list[i][j]+t_list[i-1][j-1])

print(max(t_list[N - 1]))