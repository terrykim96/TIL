E = S = M = cnt = 1

target_E , target_S , target_M = map(int,input().split())

while(True):
    if E == target_E and S == target_S and M == target_M: # target이 될때까지 전부 1씩 더해준다.
        break
    E += 1
    S += 1
    M += 1
    cnt += 1

    if E >= 16:     # 범위를 넘어가면 초기화한다.
        E -= 15
    if S >=  29:
        S -= 28
    if M >= 20:
        M -= 19

print(cnt)