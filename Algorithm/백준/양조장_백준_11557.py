T = int(input())

for _ in range(T):
    N = int(input())
    max_num = 0     # 제일 큰 숫자를 담을 기준변수 설정
    college = ""    # 그 때 대학 이름 담을 변수 설정

    for _ in range(N):
        name, num = input().split()
        num = int(num)

        if num > max_num:  # 기준 변수보다 더 크면 업데이트
            max_num = num
            college = name

    print(college)  # 최종적으로 가장 큰 대학 이름