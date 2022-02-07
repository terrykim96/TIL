T = int(input())

for i in range(T):
    days = int(input())
    price = list(map(int, input().split()))
    profit = 0
    max_price = price[-1]           # 마지막날 금액을 최대 금액으로 설정
    for j in range(days - 2, -1, -1):   # 마지막날 전날부터 거꾸로 탐색하기
        if price[j] < max_price:        # 가격이 최대 금액보다 작으면 이익에 두 가격의 차액 더하기
            profit += (max_price - price[j])
        else:                       # 가격이 최대금액보다 크면 최대 금액 바꿔주기
            max_price = price[j]

    print(f'#{i + 1} {profit}')
