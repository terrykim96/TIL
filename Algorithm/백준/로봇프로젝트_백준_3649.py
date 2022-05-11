from itertools import combinations

while True:
    try :
        X = int(input()) * 10e6
        n = int(input())

        regos = []

        for _ in range(n):
            regos.append(int(input()))

        regos.sort()        # 레고들을 크기순으로 정렬한다.

        i, j = 0, n-1       # 양쪽 끝에서부터 시작해서 더해주기 위해 i, j를 지정한다.
        flag = True         # 답이 안나오면 'danger'를 출력해야하기 때문에 flag를 지정한다. 

        while i < j:        # i가 j보다 작아지기 전까지 진행한다.
            tmp = (regos[i] + regos[j])

            if tmp == X:    # 두 조각의 합이 X이면 출력한다.이 때, 크기순으로 제일 차이가 많이 나는 조각부터 더했기 때문에 바로 break를 해준다.
                print('yes', regos[i], regos[j])
                flag = False
                break

            elif tmp < X:   # X가 합보다 크면 작은 조각의 index를 1 추가해준다.
                i += 1

            else:           # X가 합보다 작으면 큰 조각의 index를 1 감소시켜준다.
                j -= 1

        if flag:            # while문 이후에도 flag가 True면 답이 없는 것으로 danger를 출력한다.
            print('danger')

    except:
        break