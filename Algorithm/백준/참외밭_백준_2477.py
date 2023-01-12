fruit_base = int(input())
field_list = [[0] for _ in range(4)]
len_list =[]

for _ in range(6):
    direction, length = map(int, input().split())
    field_list[direction - 1].append(length)    # 방향별로 길이들을 append 해준다.
    len_list.append(length)         # 전체 길이들을 순서대로 append 해준다.

# 원래 4가지 육각형의 경우를 나누어 작은 사각형의 넓이를 구하려고 했는데, elif를 너무 많이 쓸 것 같아서 포기..
total_area = 1
tmp2 =[]
for tmp in field_list:      # 큰 사각형의 넓이를 구해준다.
    if len(tmp) == 2:       # 길이가 2개인 리스트에 들어간 길이들을 곱하면 큰 사각형의 넓이이다.
        total_area *= tmp[1]
        tmp2.append(len_list.index(tmp[1]))  # 첫번째 긴 변의 위치를구하기 위해 tmp2에 index로 append한다.

tmp2.sort()

small_area = len_list[(tmp2[0] + 3) % 6] * len_list[(tmp2[1] + 3) % 6] # 긴 변의 위치에서 +3을 한 위치의 길이들이 작은 사각형의 가로 세로이다.

ans = (total_area - small_area) * fruit_base

print(ans)