cards = []
color_cnt = {
    'R':0,
    'B':0,
    'Y':0,
    'G':0,
    }
number_cnt = [0]*10

for _ in range(5):
    color,num = map(str, input().split())
    num = int(num)
    cards.append((color, num))

    
    color_cnt[color]+=1
    number_cnt[num]+=1

cards = sorted(cards, key=lambda x: x[1])   # 카드를 현재 수를 기준으로 정렬한다.

if 5 in color_cnt.values(): #1 5장 모두 같은색, 숫자가 연속적일 때
    successive = 0
    max_num = 0

    for cnt, i in enumerate(number_cnt):
        if number_cnt[cnt] == 1:
            successive += 1
            max_num = cnt
            if successive == 5:
                break
        else:
            successive = 0
            continue
        
    if successive == 5:
        ans = 900 + max_num


if 4 in number_cnt:         #2 5장 중 4장 숫자 같을 때
    ind = number_cnt.index(4)
    ans = 800 + ind

if 3 in number_cnt and 2 in number_cnt:   #3 5장 중 3장 숫자 같고 나머지 2장도 숫자 같을 때
    ind3 = number_cnt.index(3)
    ind2 = number_cnt.index(2)
    ans = ind3*10 + ind2 + 700

if 5 in color_cnt.values():     #4 5장 모두 같은 색일 때
    max_num=0

    for cnt, i in enumerate(number_cnt):
        if number_cnt[cnt] >= 1:
            max_num = cnt
        else:
            continue
    ans = max_num + 600