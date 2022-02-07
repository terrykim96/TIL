T = int(input()) # 테스트 케이스의 개수

for i in range(T):
    numbers = list(map(int, input().split(" ")))

    ans = max(numbers)
    
    print(f'#{i+1} {ans}')
