T = int(input())

for i in range(T):
    days = int(input())
    price = list(map(int, input().split()))
    buy = 0
    product = 0
    profit = 0

    for daily_price in price:
        if daily_price < max(price):
            buy += daily_price
            product += 1
            price = price[1:]
        else:
            profit += (daily_price * product - buy)
            product =0
            buy = 0
            price = price[1:]
        print(buy, product)
    profit += (price[0] * product - buy)
    print(f'#{i + 1} {profit}')