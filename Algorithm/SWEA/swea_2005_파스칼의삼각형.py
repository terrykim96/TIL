T = int(input())

for i in range(1, T + 1):
    N = int(input())

    pascal = [[1], [1, 1]]          # 첫번째와 두번째 숫자는 미리 저장

    if N < 2:                       # 주어진 N이 2보다 작을 때 예외처리
        print(f'#{i} ')
        for j in range(N):
            print(' '.join(map(str, pascal[j])))
    
    else:                           
        print(f'#{i} ')
        print(' '.join(map(str, pascal[0])))
        print(' '.join(map(str, pascal[1])))

        for j in range(1, N-1):
            pascal_tmp = [1]

            for num in range(1, len(pascal)):   # 그 외에는 파스칼의 삼각형 규칙대로 계산
                pascal_tmp.append(pascal[j][num-1] + pascal[j][num])
            pascal_tmp.append(1)    # pascal_tmp에 현재 단계 저장 후 pascal에 append
            pascal.append(pascal_tmp)
            
            print(*pascal_tmp)
        