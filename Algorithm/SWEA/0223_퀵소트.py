def quicksort(begin, end):
    if begin > end:
        return
    t = begin
    pivot = end

    for i in range(begin, end):
        if lst[i] < lst[pivot]:
            lst[i], lst[t] = lst[t], lst[i]
            t += 1
    lst[pivot], lst[t] = lst[t], lst[pivot]
    pivot = t

    quicksort(begin, pivot - 1)
    quicksort(pivot + 1, end)

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))

    quicksort(0, N-1)

    print(f'#{test_case}', *lst)