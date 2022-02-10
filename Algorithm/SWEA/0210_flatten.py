T = 10
for test_case in range(1, T + 1):
    N = int(input())
    box = list(map(int, input().split()))
    height = [0] * 101  # 1~100까지 높이를 저장할 리스트 생성
    minimum = 1000
    maximum = 0
    
    for i in range(100):    # 높이 최댓값과 최솟값을 지정
        height[box[i]] += 1
        if maximum < box[i]:
            maximum = box[i]
        if minimum > box[i]:
            minimum = box[i]

    while N > 0 and minimum < (maximum - 1):    # 덤프를 모두 실행하거나 평탄화가 완료될때까지
        height[minimum + 1] += 1    # 높이 최신화 (min높이의 박스 -1 (min+1)높이 박스 +1
        height[minimum] -= 1        # (max높이의 박스 -1 (max-1)높이 박스 +1)

        height[maximum] -= 1
        height[maximum - 1] += 1

        if height[minimum] == 0:    # 박스 개수가 0이면 min, max 새로 설정
            minimum += 1
        if height[maximum] == 0:
            maximum -= 1
        
        N -= 1

    print(f'#{test_case} {maximum - minimum}')