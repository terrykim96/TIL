N = int(input())

table = []

for i in range(N):
    table.append(list(map(int, input().split())))

ans = [0 for i in range(N + 1)]

for i in range(N - 1, -1, -1):      # 백만장자처럼 뒤에서부터 시작해서 N번째날의 금액을 정해준다.
    if (i + table[i][0]) > N:       # (N번째 날 기준 수익 + Tn만큼 지난 후 수익)과 (N + 1번째날 수익) 중 더 큰게 N번째 날 수익
        ans[i] = ans[i + 1]         
    else:                           
        ans[i] = max(table[i][1] + ans[i + table[i][0]], ans[i + 1])

print(ans[0])