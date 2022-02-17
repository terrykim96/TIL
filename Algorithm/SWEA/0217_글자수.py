T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    dic ={}
    for char in str1:
        dic.update({char: 0})
    
    for char in str2:
        try:
            dic[char] += 1
        except:
            pass
    
    ans = sorted(dic.items(), key = lambda x: x[1])[-1][1]
    print(f'#{test_case} {ans}')