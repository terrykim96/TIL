T = int(input())

for test_case in range(1, T + 1):
    string = input()
    ans = ''

    for i in range(len(string) - 1, -1, -1):
        if string[i] == 'p':
            ans += 'q'
        elif string[i] == 'q':
            ans += 'p'
        elif string[i] == 'b':
            ans += 'd'
        elif string[i] == 'd':
            ans += 'b'
    print(f'#{test_case} {ans}')