N, K = map(int, input().split())
medals = []

for _ in range(N):
    medals.append(list(map(int, input().split())))

medals.sort(key=lambda x : (-x[1], -x[2], -x[3]))

for i in range(N):
    if medals[i][0] == K:
        index = i

for i in range(N):
    if medals[index][1:] == medals[i][1:]:
        print(i + 1)
        break