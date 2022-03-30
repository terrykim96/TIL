def babygin(num, cnt_lst):  # 카드숫자, 카운팅리스트
    cnt_lst[num] += 1
    flag = 0
    i = 0
    while i < 8:
        if cnt_lst[i] >= 3:  # triplet check
            flag = 1
            break
        if cnt_lst[i] and cnt_lst[i + 1] and cnt_lst[i + 2]:  # run check
            flag = 1
            break
        i += 1
    if flag == 1:
        return True

T = int(input())

for test_case in range(1, T + 1):
    card_lst = list(map(int, input().split()))
    cnt_1, cnt_2 = [0]*10, [0]*10

    ans = 0
    for i in range(0, len(card_lst), 2):
        if babygin(card_lst[i], cnt_1):
            ans = 1
            break
        if babygin(card_lst[i+1], cnt_2):
            ans = 2
            break
    
    print(f'#{test_case} {ans}')