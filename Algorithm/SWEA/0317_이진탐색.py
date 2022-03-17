def in_order(v):
    if v:
        in_order(ch1[v])
        ans.append(v)
        in_order(ch2[v])
 
 
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ch1 = [0] * (N + 1)
    ch2 = [0] * (N + 1)
      
    for i in range(2, N + 1):
        if not ch1[i // 2]:
            ch1[i // 2] = i
        else:
            ch2[i // 2] = i
      
    ans = []
    in_order(1)
 
    print(f'#{test_case}', ans.index(1) + 1, ans.index(N//2) + 1)