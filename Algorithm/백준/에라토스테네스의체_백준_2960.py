N, K = map(int, input().split())
cnt = 0
nums = [True] * (N + 1)

for i in range(2, N + 1):
    for j in range(i, N + 1, i):    # 배수가 나올 때마다 true를 false로 바꿔주면서 cnt를 늘려준다.
        if nums[j]:
            nums[j] = False
            cnt += 1

            if cnt == K:            # cnt가 K가 되면 그때의 j를 return한다.
                print(j)