T = int(input())

for test_case in range(1, T + 1):
    string = input()
    bar = 0
    ans = 0

    for i in range(len(string)):
        if string[i] == '(':
            if string[i + 1] == ')':
                ans += bar
            else:
                bar += 1
        else:
            if string[i - 1] == '(':
                continue
            else:
                ans += 1
                bar -= 1

    print(f'#{test_case} {ans}')