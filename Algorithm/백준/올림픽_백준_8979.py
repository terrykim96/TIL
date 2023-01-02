N, K = map(int, input().split())
medals = []

for _ in range(N):
    medals.append(list(map(int, input().split())))

medals.sort(key=lambda x : (-x[1], -x[2], -x[3]))   # 메달 수 순서대로(금, 은, 동) sort해준다.

for i in range(N):      # 주어진 국가의 index를 구한다.
    if medals[i][0] == K:
        index = i

for i in range(N):      # 메달 개수가 같은 국가의 등수를 구한다.
    if medals[index][1:] == medals[i][1:]:
        print(i + 1)
        break