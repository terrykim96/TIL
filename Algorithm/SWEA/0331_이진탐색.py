T = int(input())


for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    # A를 정렬해야 한다고 했으므로 먼저 정렬
    A.sort()
    # 숫자 갯수를 셀 변수 초기화
    cnt = 0
    # B의 원소들을 확인하기 위해서 M으로 B의 길이를 설정
    for i in range(M):
        # 초기 left, right 값 설정
        L = 0
        R = N - 1
        # target 변수 설정
        target = B[i]
        # 그전과정을 저장해주는 변수
        history = 0  # 1:left , 2:right
        # L이 R을 넘어갈 때 까지 검사
        while L <= R:
            # 문제조건에 나온대로 중앙값 설정
            mid = (L+R)//2
            # 만약 중앙값하고 같아진다면 찾은것
            if target == A[mid]:
                cnt += 1
                break
            # 만약 중앙값 보다 클때 오른쪽으로 가야한다.
            elif target > A[mid]:
                # 하지만 이미 오른쪽으로 온상태라면
                if history == 2:
                    # 못찾는케이스
                    break
                else:
                    # 아니라면 L을 갱신하고
                    L = mid + 1
                    # 기록하기
                    history = 2
            # 그반대로 작은경우에는 왼쪽으로가야함
            elif A[mid] > target:
                # 하지만 이미 왼쪽으로 온상태라면 종료
                if history == 1:
                    break
                else:
                    # 아니면 똑같이 해줌
                    R = mid - 1
                    history = 1

    print(f'#{test_case} {cnt}')