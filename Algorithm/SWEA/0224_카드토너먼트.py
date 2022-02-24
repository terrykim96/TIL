def rps(x, y):  # 가위바위보 룰
    if card[x] == card[y]:
        return x
    elif card[x] - card[y] == 1 or card[x] - card[y] == -2:
        return x
    return y

def divide(start, end):     # 둘로 나눠서 가위바위보 하기 (재귀로 돌려서 원소가 하나가 될 때까지)
    if start == end:
        return start
    
    a = divide(start, (start + end) // 2)
    b = divide((start + end) // 2 + 1, end)
    
    return rps(a, b)

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    card = list(map(int, input().split()))

    ans = divide(0, N-1) + 1    # 학생 번호는 1번부터이므로 +1 해준다.

    print(f'#{test_case} {ans}')