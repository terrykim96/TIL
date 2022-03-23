T = int(input())

for test_case in range(1, T + 1):
    num = input()
    ans = []

    for i in range(0, len(num), 7):
        tmp = num[i : i + 7]
        ans.append(int(tmp, 16))
    print(f'#{test_case}', *ans)