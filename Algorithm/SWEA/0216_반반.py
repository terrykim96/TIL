T = int(input())

for test_case in range(1, T + 1):
    string = input()
    tar1 = string[0]

    if tar1 not in string[1:]:
        ans = 'No'
    else:
        for i in range(1, len(string) - 1):
            ans = 'No'
            if tar1 != string[i]:
                tar2 = string[i]
                if tar2 in string[i + 1 :]:
                    ans = 'Yes'
                    break
    print(f'#{test_case} {ans}')