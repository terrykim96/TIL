n = int(input())

nums_pileup = 1  # 벌집의 개수, 1개부터 시작
cnt = 1

while n > nums_pileup :
    nums_pileup += 6 * cnt  # 벌집이 6의 배수로 증가
    cnt += 1  # 반복될 때마다 cnt 1씩 증가

print(cnt)