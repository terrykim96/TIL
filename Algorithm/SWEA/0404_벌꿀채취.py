from itertools import combinations

def issafe(x, y):
    tmp = 0
    for i in range(M):
        if -1 < y+i < N:
            tmp += 1

    if tmp == M:
        return 1

    else:
        return 0


def cal(x, y):
    cap = []
    for i in range(M):
        tmp = honey[x][y+i]
        cap.append(tmp)

    subsum = []
    for j in range(M):
        combs = combinations(cap, M-j)
        for comb in combs:
            if sum(comb) <= C:
                summ = 0
                for k in comb:
                    summ += k**2
                subsum.append(summ)

    return max(subsum)


def profit(i, j):
    prof = cal(i, j)

    tmp = []
    for a in range(i, N):
        if a == i:
            k = j + M
        else:
            k = 0

        for b in range(k, N):
            if issafe(a, b):
                tmp.append(cal(a, b))
    if tmp:
        return max(tmp) + prof
    else:
        return 0


T = int(input())
for test_case in range(1, T + 1):

    N, M, C = map(int, input().split())

    honey = []
    for _ in range(N):
        honey.append(list(map(int, input().split())))

    ans = 0
    for i in range(N):
        for j in range(N):
            if issafe(i, j):
                ans = max(ans, profit(i, j))

    print(f'#{test_case} {ans}')