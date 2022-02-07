T = int(input())
for i in range(T):  # 각각의 테스트 케이스에 대해
    words = input()
    for j in range(2, 12):  # 패턴의 길이가 1~10자인데, 안의 조건문에서 (j + 1)을 사용하기 위해 range(2,12)를 사용
        word_list = []      # 패턴의 길이가 달라질 때마다 리스트를 초기화
       
        try:                # 리스트 인덱스 범위 내에서만 사용
            for k in range(30 // j):    # 슬라이싱 내에서 j에 k를 곱해서 사용하기 위해 (30 // j)까지읩 range

                word_list.append(words[k * j : (k+1) * j])
            
            if len(set(word_list)) == 1:
                print(f'#{i+1} {j}')
                break
        except:
            continue