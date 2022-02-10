T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    a = b = c = d = e = 0
    
    while N % 2 == 0:   # 소인수로 가능할 때까지 계속 나눠서 지수에 추가
        N = N // 2
        a += 1
    while N % 3 == 0:
        N = N // 3
        b += 1
    while N % 5 == 0:
        N = N // 5
        c += 1
    while N % 7 == 0:
        N = N // 7
        d += 1
    while N % 11 == 0:
        N = N // 11
        e += 1
    
    print(f'#{test_case} {a} {b} {c} {d} {e}')