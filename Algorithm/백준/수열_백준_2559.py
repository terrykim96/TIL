N, K = map(int, input().split())
temp_list = list(map(int, input().split()))

# 처음에 sum으로 k개씩 묶어서 sum의 최댓값을 구하려 했지만 시간초과 문제 발생
# sum함수의 사용을 줄이기 위해 첫 k개만큼의 합을 기본값으로 저장하고
# for문으로 여기에 다음 온도를 추가하고, 처음 온도는 빼주는 방식으로 품

temperature = sum(temp_list[:K])
ans = temperature               # 초기값을 0으로 했다가 온도합이 음수인 경우 발생해서 변경

for i in range(K, N):           # 다음 온도를 추가하기 위해 K부터 반복문 시작
    temperature += temp_list[i]
    temperature -= temp_list[i - K] # 처음 온도 빼주기

    if ans < temperature:       # 최대 온도 합 저장
        ans = temperature

print(ans)