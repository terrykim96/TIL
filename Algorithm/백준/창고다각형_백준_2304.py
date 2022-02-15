N = int(input())
dic = {}
loc = []
area = 0
height = 0
for _ in range(N):
    L, H = map(int, input().split())
    dic[L] = H
    loc.append(L)
loc.sort()

tmp = loc[0]
for i in range(1, N):
    if height < dic[loc[i - 1]]:
        height = dic[loc[i - 1]]
        area += height * (loc[i] - tmp)
        tmp = loc[i]