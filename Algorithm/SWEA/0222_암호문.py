T = 10

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    K = int(input())
    ans = arr[:10]
    orders = list(map(str, input().split()))

    for i in range(len(orders)):
        if orders[i] == 'I':
            x, y = int(orders[i + 1]), int(orders[i + 2])
            if x >= 10:
                continue

            s = orders[i + 3 : i + 3 + int(y)]

            tmp1, tmp2 = ans[:x], ans[x:]
            ans = tmp1 + s + tmp2
            ans = ans[:10]
    print(f'#{test_case}', *ans)