N = int(input())

room = []
cnt_w = 0
cnt_h = 0
position_w = 0
position_h = 0

for _ in range(N):
    room.append(input())

# 가로와 세로에 대해 전부 구해서 출력한다.
for i in room:  # 점과 벽을 기준으로 2자리 이상이 있다면 누울 자리가 있다는 뜻이다.
    cnt_w = 0
    for j in i:
        if j == '.':
            cnt_w += 1

        else:
            if cnt_w >= 2:
                position_w += 1
            cnt_w = 0

    if cnt_w > 1:   # 가로
        position_w += 1
    

for i in range(N):
    cnt_h = 0
    for j in range(N):
        if room[j][i] == '.':
            cnt_h += 1

        else:
            if cnt_h >= 2:
                position_h += 1
            cnt_h = 0

    if cnt_h > 1:   # 세로
        position_h += 1
    
print(position_w, position_h)