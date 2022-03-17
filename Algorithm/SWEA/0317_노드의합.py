T = int(input())
for test_case in range(1, T + 1):
 
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
 
    for _ in range(M):
        p, c = map(int, input().split())
        tree[p] = c
         
    if not N % 2:
        tree.append(0)

    for i in range((N //2)*2, 1, -2):
        tree[i // 2] = tree[i] + tree[i + 1]

    print(f'#{test_case} {tree[L]}')