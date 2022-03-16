def pre_order(v):
    if v:
        ans.append(v)
        pre_order(ch1[v])
        pre_order(ch2[v])
 
T = int(input())
 
for test_case in range(1, T + 1):
    V = int(input())
    arr = list(map(int, input().split()))
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
     
    for i in range(len(arr) // 2):
        p, c = arr[2 * i], arr[2 * i + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c
 
    ans = []
     
    pre_order(1)
    print(f'#{test_case}', *ans)