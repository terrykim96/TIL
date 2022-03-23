def ten(num):
    num = num[::-1]
    answer = 0

    for i in range(len(num)):
        if i == 0:
            x = int(num[i])
            answer += x
        else:
            if num[i] == '1':
                answer = answer + (2 ** i)
    return answer

T = int(input())

for test_case in range(1, T + 1):
    num = input()
    ans = []

    for i in range(0, len(num), 7):
        tmp = num[i : i + 7]
        ans.append(ten(tmp))
    print(f'#{test_case}', *ans)
    