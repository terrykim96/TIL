def tree(v):
    global ans
    if v:
        tree(left[v])
        tree(right[v])
        ans += 1
 
T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int,input().split())
    lst = list(map(int,input().split()))
    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(E):
        if left[lst[i * 2]]==0:
            left[lst[i * 2]] = lst[i * 2 + 1]
        else:
            right[lst[i * 2]] = lst[i * 2 + 1]

    ans = 0
    tree(N)

    print(f'#{test_case} {ans}')