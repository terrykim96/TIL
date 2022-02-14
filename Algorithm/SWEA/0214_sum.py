for test_case in range(1, 11):
    T = int(input())
    numbers = []
    
    for i in range(100):
        numbers.append(list(map(int, input().split())))
    
    maximum = 0
    
    for i in range(100):        # 같은 행끼리 더하기
        tmp = 0
        for j in range(100):
            tmp += numbers[i][j]
        if maximum < tmp:
            maximum = tmp
    
    for j in range(100):        # 같은 열끼리 더하기
        tmp = 0
        for i in range(100):
            tmp += numbers[i][j]
        if maximum < tmp:
            maximum = tmp
    
    tmp = 0
    for i in range(100):        # 대각선 더하기
        tmp += numbers[i][i]
    if maximum < tmp:
        maximum = tmp

    tmp = 0
    for i in range(100):        # 역대각선 더하기
        tmp += numbers[i][99 - i]
    if maximum < tmp:
        maximum = tmp
    
    print(f'#{test_case} {maximum}')