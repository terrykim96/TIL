x, y, w, s = map(int, input().split())

tmp1 = (x + y) * w          # 평행으로만 이동

if (x + y) % 2 == 0:    # 대각선으로만 이동
    tmp2 = max(x, y) * s

else:                   # 대각선이동 + 평행이동 1번
    tmp2 = (max(x, y) - 1) * s + w

tmp3 = (min(x, y) * s) + (abs(x - y) * w)   # 평행이동 + 대각선이동

print(min(tmp1, tmp2, tmp3))