case_num = int(input()) # 테스트 케이스의 개수
for i in range(case_num):
    numbers = list(map(int, input().split(" ")))

    ans = 0
    # 1. numbers를 순회하면서
    for num in numbers:
        # 2. num이 홀수인지 판별
        if num%2 == 1:
            # 3. 홀수라면 ans에 더하기
            ans += num
    print('#' + str(i+1)+ ' ' + str(ans))