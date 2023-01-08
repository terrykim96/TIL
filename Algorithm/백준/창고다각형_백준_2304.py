N = int(input())
dic = {}
loc = []
bld = []
area = 0

for _ in range(N):  # 가장 높은 지점을 기준으로 반반 나눠서 양쪽 끝에서부터 중앙으로 진행하면서
    L, H = map(int, input().split())
    dic[L] = H
    loc.append(L)
    bld.append(H)

high = loc[bld.index(max(bld))]

height = 0
for i in range(high + 1):   # 각 x축 지점의 높이를 더해준다 (높이 = 현재까지의 기둥 높이 중 최댓값)
    if dic.get(i):
        if height < dic.get(i):
            height = dic.get(i)

    area += height

height = 0
for i in range(max(loc), high, -1):
    if dic.get(i):
        if height < dic.get(i):
            height = dic.get(i)

    area += height

print(area)