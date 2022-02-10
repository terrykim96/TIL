T = int(input())

for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    char_list = list(map(int, input().split()))
    cnt = 0
    i = 0
    while True: # 정류소 번호를 하나씩 늘리면서 
        i += K

        if i >= N:  # 정류소 번호가 N보다 커지면 break
            break

        for j in range(i, i - K, -1):   # 정류소 + K부터 1씩 줄이면서
            if j in char_list:          # 충전소 리스트에 있으면 정류장 옮기기
                cnt += 1
                i = j
                break
        else:       # 못찾으면 0 출력 break
            cnt = 0
            break
        

    print(f'#{test_case} {cnt}')