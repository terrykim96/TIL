def in_order(v):
    if v <= N:
        in_order(v * 2)
        ans.append(tree[v])
        in_order(v * 2 + 1)

T = 10

for test_case in range(1, T + 1):
    N = int(input())
    tree = [0] * (N + 1)

    for i in range(N):
        tmp = list(map(str, input().split()))
        tree[int(tmp[0])] = tmp[1]
    
    ans = []
    in_order(1)
    print(f'#{test_case}', ''.join(ans))