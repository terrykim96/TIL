for t in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))
    ans = 0

    for i in range(2, N-2):
        home = buildings[i]
        tmp = buildings[i-2 : i] + buildings[i+1 : i+3]

        maximum = 0
        for height in tmp:
            if maximum < height:
                maximum = height
        if maximum < home:
            ans += (home - maximum)

    print(f'#{t} {ans}')