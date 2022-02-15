def binary_count(N, key):
    start = 1
    end = N
    cnt = 0
    if start == key or end == key:
        return cnt

    while start <= end:
        middle = (start + end) // 2

        cnt += 1
        if middle == key:
            return cnt
        elif middle > key:
            end = middle
        else:
            start = middle

T = int(input())

for test_case in range(1, T + 1):
    P, A, B = map(int, input().split())

    if binary_count(P, A) < binary_count(P, B):
        print(f'#{test_case} A')
    elif binary_count(P, A) > binary_count(P, B):
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} 0')