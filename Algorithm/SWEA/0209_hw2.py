T = int(input())

for t in range(1, T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    ans = 0
    
    for i in range(N):
        cnt = 0
        for j in range(i+1, N):
            if num_list[i] > num_list[j]:
                cnt += 1
        if ans < cnt:
            ans = cnt

    print(f'#{t} {ans}')