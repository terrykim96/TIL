bingo = []
call_num = []

for _ in range(5):  # 빙고와 사회자가 부른 숫자 저장
    bingo.append(list(map(int, input().split())))

for _ in range(5):
    call_num += list(map(int, input().split()))

check = [0] * 12    # 부른 숫자 저장 리스트 0~4는 가로 / 5~9는 세로 / 10, 11은 대각방향
line = 0            # 빙고 갯수 변수 지정
tmp = False         # while문으로 line이 3이 될 때까지 하려 했는데 안돼서 break 사용

for n in range(25): #사회자가 부를 때
    if tmp == True:
        break
    for i in range(5):                      #빙고탐색
        if tmp == True:
            break
        for j in range(5):
            if tmp == True:
                break
            if call_num[n] == bingo[i][j]:  # 사회자가 부른 숫자와 같은 위치의 숫자를
                bingo[i][j] = 0             # 0으로 바꾸고 변경 체크
                check[i] += 1
                check[j+5] += 1
                
                if i == j:              # 대각
                    check[10] += 1
                if i + j == 4:          # 반대대각
                    check[11] += 1

                for c in range(12):     # 바뀐것 갯수 저장하는 리스트 탐색해서
                    if check[c] == 5:   # 5번 바뀌었으면
                        check[c] = 0    # 초기화시키고 빙고처리
                        line += 1
                        if line == 3:
                            tmp = True
                            break
print(n)