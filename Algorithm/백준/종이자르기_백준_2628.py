m, n = map(int, input().split())    # 가로와 세로 길이를 입력받는다.
cut = int(input())                  # 자르는 횟수를 입력받는다.

row1 =[0, n]                        # 가로, 세로로 자를 행동을 저장할 리스트를 생성한다.
column1 = [0, m]                    # 이 때, 잘린 넓이를 계산하기 위해 0과 끝 길이를 넣어준다.

for i in range(cut):                # 자르는 횟수만큼 가로, 세로로 자르는 행동을 입력 받아 각 리스트에 저장한다.
    tmp1, tmp2 = map(int, input().split())
    if not tmp1:
        row1.append(tmp2)
    else:
        column1.append(tmp2)

row1.sort()                         # 행동 리스트를 오름차순으로 정렬한다.
column1.sort()

cutted_row = []                     # 잘려진 조각들을 저장할 리스트를 생성한다.
cutted_column = []

for i in range(1, len(row1)):       # 가로, 세로로 잘려진 절편의 크기를 행동 리스트의 차로 계산한다.
    cutted_row.append(row1[i] - row1[i-1])

for i in range(1, len(column1)):    # 절편의 크기 = 다음 행동 - 전 행동
    cutted_column.append(column1[i] - column1[i-1])

ans = sorted(cutted_row)[-1] * sorted(cutted_column)[-1]    # 절편 중 가장 큰 크기를 출력한다.

print(ans)