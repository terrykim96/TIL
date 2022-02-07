from statistics import mean

T = int(input())

for i in range(1, T+1):
    num = list(map(int, input().split()))
    num.sort()                              # 입력받은 숫자 리스트를 오름차순으로 정렬한다.
    ans = int(round(mean(num[1:-1]),0))     # 양 끝(최소, 최대)을 제외한 나머지 수의 평균을 구한다.
    print(f'#{i} {ans}')