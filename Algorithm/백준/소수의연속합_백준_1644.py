#4000000이하의 모든 소수를 에라토스테네스의 체로 구해준다.
prime_flag = [True] * 4000001

for i in range(2, int(4000001 ** 0.5)):
    if prime_flag[i]:
        for j in range(i+i, 4000001, i):
            prime_flag[j] = False 

prime_num = [i for i, j in enumerate(prime_flag) if j == True and i >=2 ]

# 시작지점과 끝 지점을 정해두고 (합 < 정해진 수)일 때는 끝 지점을 하나 더해주고, 반대일 때는 반대로 해준다.
ans = 0
start = 0
end = 0

N = int(input())
while end <= len(prime_num):
    temp_sum = sum(prime_num[start:end])

    if temp_sum == N:   # 합이 정해진 수일 때, 답 +1, 끝지점 +1 해준다.
        ans += 1
        end += 1

    elif temp_sum < N:  # 정해진 수보다 작을 때, 끝지점 +1 해준다.
        end += 1

    else:               # 정해진 수보다 클 때, 시작지점 +1 해준다.
        start += 1

print(ans)