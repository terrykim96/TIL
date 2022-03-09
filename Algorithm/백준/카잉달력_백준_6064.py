for _ in range(int(input())):
    M, N, x, y = map(int, input().split())
    flag = 1
    while x <= M * N :     
        if x % N == y % N:  # x를 N으로 나눈 나머지가 y를 N으로 나눈 나머지랑 같을 때까지 x에 M을 더해준다.
            print(x)
            flag = 0
            break
        x += M              # x에 M을 더하면 똑같이 x이기 때문에 사실상 x는 고정이다.
    if flag:                # 끝까지 해를 찾지 못했다면 -1을 출력한다.
        print(-1)