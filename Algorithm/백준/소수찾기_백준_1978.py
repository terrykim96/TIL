N = int(input())
numbers = list(map(int, input().split()))
ans = 0

for x in numbers:   # 숫자들 중에서
    for i in range(2, x + 1): # 소수 판별한다.
        if x % i == 0:      # 2보다 큰 약수가 있는지 판단한다.(나머지가 0이면 약수)
            if x == i:      # 자기만 약수로 갖고있으면 소수이므로 (개수 + 1) 해준다.
                ans += 1
      
            break         # 다음 숫자로 넘어간다.

print(ans)