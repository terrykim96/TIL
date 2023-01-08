T = int(input())

for _ in range(T):
    n = int(input())
    data = list(map(int,input().split()))
    ans = 0 
    max_price = data[-1]                   # 맨 마지막을 최댓값으로 설정한다.
    
    for i in range(n - 2, -1, -1):  # 리스트 마지막부터 거꾸로 탐색한다.
        if data[i] > max_price:            # 오늘 가격이 가장 높다면 
            max_price = data[i]

        else:
            ans += max_price - data[i]    # 오늘 가격이 최대가 아니라면 (최대 - 지금가격)만큼 더한다 
    
    print(ans)