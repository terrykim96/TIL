T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_list = [0] * 10     # 0~9 숫자 개수 저장할 리스트 생성
    number = input()
    ans_idx = 0
    ans_num = 0

    for i in number:        # 리스트의 각 인덱스에 숫자 개수 추가해서 저장
        num_list[int(i)] += 1
    
    for idx, num in enumerate(num_list):    # 가장 많은 카드의 번호와 개수 출력
        if ans_num <= num:
            ans_num = num
            ans_idx = idx
    print(f'#{test_case} {ans_idx} {ans_num}')