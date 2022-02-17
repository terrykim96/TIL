T = int(input())

for test_case in range(1, T + 1):
    A, B = map(str, input().split())
    cnt = len(A)

    i = 0
    while i < (len(A) - len(B) + 1):
        if A[i : i + len(B)] == B:
            cnt -= (len(B) - 1)
            i += len(B)
        else:
            i += 1

    print(f'#{test_case} {cnt}')