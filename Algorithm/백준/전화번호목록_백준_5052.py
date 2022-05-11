T = int(input())

for _ in range(T):
    N = int(input())
    numbers = []

    for _ in range(N):
        numbers.append(input())

    numbers.sort()                  # string을 sort하면 겹치는 숫자가 있는 번호들이 앞뒤로 정렬된다.

    flag = True

    for i in range(N - 1):          # 바로 다음 순서와 비교해준다.
        length = len(numbers[i])
        if numbers[i] == numbers[i + 1][:length]:
            flag = False
            break

    if flag:
        print('YES')
    else:
        print('NO')