N, L = map(int, input().split())
crack = list(map(int, input().split()))

crack.sort()

start = crack[0]
end = crack[0] + L
ans = 1

for i in range(N):
    if start <= crack[i] < end:     # 시작 지점에서부터 테이프 길이 L까지의 범위에 구멍이 있으면 한번에 막을 수 있다.
        continue
    else:
        start = crack[i]            # 범위를  벗어나면 새로운 시작지점을 정해주고 테이프 갯수를 1개 늘려준다.
        end = crack[i] + L
        ans += 1

print(ans)