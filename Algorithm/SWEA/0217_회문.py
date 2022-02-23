def is_round(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    lst = []
    for _ in range(N):
        lst.append(input())

    for i in range(N):
        for j in range(N - M + 1):
            string = lst[i][j : M + j]
            if is_round(string):
                print(f'#{test_case} {string}')
                break

    for i in range(N):
        for j in range(N - M + 1):
            tmp = ''
            for k in range(M):
                tmp += lst[j + k][i]
            if is_round(tmp):
                print(f'#{test_case} {tmp}')
                break