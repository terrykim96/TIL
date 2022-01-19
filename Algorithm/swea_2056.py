T = int(input())

for i in range(1, T+1):
    ymd = input()
    date = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    
    if int(ymd[4:6]) <= 0 or int(ymd[4:6]) > 12 or int(ymd[6:]) > date[int(ymd[4:6]) - 1]:
        print(f'#{i} -1')
    else:
        print(f'#{i} {ymd[:4]}/{ymd[4:6]}/{ymd[6:]}')