nums = [True] * 1000001

for i in range(2, 1001):        # 에라토스테네스의 체로 소수를 구해준다. 이때 1000까지만 구해주면 된다.
    if nums[i]:
        for k in range(i + i, 1000001, i):
            nums[k] = False

while True:
    n = int(input())

    if n == 0: break

    for i in range(3, len(nums)):
        if nums[i] and nums[n-i]:   # 둘다 소수일 때 그 값을 출력해준다.
            print(n, "=", i, "+", n-i)
            break    