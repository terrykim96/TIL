N, K = map(int, input().split()) 
coin = list()
for i in range(N):
    coin.append(int(input()))

cnt = 0
for i in reversed(range(N)):
    cnt += K//coin[i] #카운트 값에 K를 동전으로 나눈 몫을 더해줌
    K = K % coin[i] # K는 동전으로 나눈 나머지로 계속 반복

print(cnt)