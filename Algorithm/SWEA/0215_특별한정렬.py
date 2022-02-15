T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
        
    for i in range(5):
        ans.append(lst[-1 - i])
        ans.append(lst[i])
    print(f'#{test_case}', *ans)