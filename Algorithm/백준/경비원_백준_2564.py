W, H = map(int, input().split())
N = int(input())
distance = []
for _ in range(N + 1):      # (0,0)부터 상점과 동근이 까지의 거리를 각각 구한다.
    dr, leng = map(int, input().split())
    if dr == 1:
        distance.append(leng)
    elif dr == 2:
        distance.append(W + H + W - leng)
    elif dr == 3:
        distance.append(W + H + W + H - leng)
    else:
        distance.append(W + leng)

ans = 0

for i in range(N):          # 시계방향과 반시계방향에 대해 동근이와 상점 사이의 거리를 구해서 ans에 더해준다.
    clock = abs(distance[-1] - distance[i])
    anticlock = 2 * (W + H) - clock

    ans += min(clock, anticlock)

print(ans)