T = int(input())
num_str = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for test_case in range(1, T + 1):
    _, N = map(str, input().split())
    lst = list(map(str, input().split()))
    new_lst = []
    for string in lst:
        for i in range(len(num_str)):
            if string == num_str[i]:
                new_lst.append(i)
    
    for i in range(len(new_lst) - 1):
        for j in range(i + 1, len(new_lst)):
            if new_lst[i] > new_lst[j]:
                new_lst[i], new_lst[j] = new_lst[j], new_lst[i]

    print(f'#{test_case}', end= ' ')
    
    for num in new_lst:
        print(num_str[num], end=' ')