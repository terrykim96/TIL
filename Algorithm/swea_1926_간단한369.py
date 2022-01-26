N = int(input())

for i in range(N):
    if '3' in str(i+1):         # 숫자에 3이 들어가면
        cnt = 0            
        for j in str(i+1):  # 3, 6, 9가 들어가는 갯수만큼 cnt를 증가시킴
            if j in ['3', '6', '9']:
                cnt += 1
        print('-'*cnt, end= ' ')    # cnt 갯수만큼 '-' 출력
    elif '6' in str(i+1):   # 6과 9에 대해서도 같은 방식으로 진행
        cnt = 0
        for j in str(i+1):
            if j in ['3', '6', '9']:
                cnt += 1
        print('-'*cnt, end= ' ')
    elif '9' in str(i+1):
        cnt = 0
        for j in str(i+1):
            if j in ['3', '6', '9']:
                cnt += 1
        print('-'*cnt, end= ' ')       
    else:
        print(i+1, end=' ')     # 3 6 9 아무것도 없다면 숫자 출력
# ---------------------------------------------------------------------

# check_num 세개에 각각 3, 6, 9 저장
check_num1, check_num2, check_num3 = '3', '6', '9'

# 숫자의 문자열에서 check_num을 세어 총 숫자를 clap_num에 저장
for num in range(1, N+1):
    clap_num = str(num).count(check_num1) + str(num).count(check_num2) + str(num).count(check_num3)
    if not clap_num:        # clap_num이 0이면 숫자 출력
        print(num, end= '')
    print('-'*clap_num, end= ' ')   # 0이 아니면 숫자만큼 '-' 출력