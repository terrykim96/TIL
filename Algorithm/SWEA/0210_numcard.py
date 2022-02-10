T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num_list = [0] * 10
    number = input()
    ans_idx = 0
    ans_num = 0

    for i in number:
        num_list[int(i)] += 1
    
    for idx, num in enumerate(num_list):
        if ans_num <= num:
            ans_num = num
            ans_idx = idx
    print(f'#{test_case} {ans_idx} {ans_num}')