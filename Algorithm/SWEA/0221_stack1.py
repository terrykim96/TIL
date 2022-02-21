T = int(input())
for test_case in range(1, T + 1):
    cols = list(input())
    arr = []
    cnt1 = 0
    cnt2 = 0
    for i in cols:
        if i =='(':
            arr.append(i)
            cnt1 += 1
        elif i == ')':
            if arr:
                arr.pop()
                cnt2 += 1
            else:
                cnt2 += 1
    if arr or cnt1 != cnt2:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')