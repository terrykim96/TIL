from statistics import mean


case_num = int(input()) # 테스트 케이스의 개수
for i in range(case_num):
    numbers = list(map(int, input().split(" ")))

    ans = round(mean(numbers))
    print(f'#{i+1} {ans}')