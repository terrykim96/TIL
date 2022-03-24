N = int(input())
p = []
for i in range(N):  # p[0]에는 빨강, 초록, 파랑의 첫번째 값을 넣어준다.
    p.append(list(map(int, input().split())))
for i in range(1, len(p)):  # 빨강일때는 이전 초록과 파랑 집의 dp 중 작은 값과 빨강 값의 합을 넣어준다.
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]   # p[i][0] i번째를 빨강으로 칠했을때 
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]   # p[i][1] i번째를 초록으로 칠했을때
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]   # p[i][1] i번째를 파랑으로 칠했을때
print(min(p[N - 1][0], p[N - 1][1], p[N - 1][2]))