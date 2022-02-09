w, h = map(int, input().split())
x, y = map(int, input().split())
t = int(input())

# 직접 시뮬레이션 하면 시간초과가 나와서 다르게 생각해서 풀었습니다..
# x와 y는 각각 x, y축 위에서만 움직임

w_list = list(range(w))
w_list.extend(list(range(w, 0, -1))) # [0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]

h_list = list(range(h))
h_list.extend(list(range(h, 0, -1))) # [0, 1, 2, 3, 4, 3, 2, 1] 

x_t = w_list[(x+t) % (2*w)] # 처음 시작 x, y에서 t만큼 움직이는데 벽에 닿을때마다 방향이 바뀌므로 이렇게 계산해준다.
y_t = h_list[(y+t) % (2*h)]

print(x_t, y_t)