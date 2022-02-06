from collections import defaultdict

round = int(input())
for round_num in range(round):
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    
    A.pop(0)    #딱지의 개수 부분 제거
    B.pop(0)

    A_dic, B_dic = defaultdict(int), defaultdict(int)   # 각 모양의 갯수를 판단하기 위한 딕셔너리 생성
    for num in A:         # 이 때 value값을 +=으로 하나씩 늘려주기 위해 defaultdict를 사용해서 key가 없다면 기본값을 지정
        A_dic[num] += 1
    for num in B:
        B_dic[num] += 1
    
    #같은 모양 기준, 개수가 더 많은 쪽을 프린트
    #전부 다 같으면 D
    for shape in range(4,0,-1):
        if A_dic[shape] > B_dic[shape] :
            print('A')
            break
        elif A_dic[shape] < B_dic[shape] :
            print('B')
            break
    else :
        print('D')