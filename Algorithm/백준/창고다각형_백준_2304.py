N = int(input())
dic = {}
loc = []
bld = []
area = 0

for _ in range(N):
    L, H = map(int, input().split())
    dic[L] = H
    loc.append(L)
    bld.append(H)

high = loc[bld.index(max(bld))]
height = 0
for i in range(high + 1):
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