T = int(input())

for i in range(1, T + 1):
    N = int(input())

    pascal = [[1], [1, 1]]

    if N < 2:
        print(f'#{i} ')
        for j in range(N):
            print(' '.join(map(str, pascal[j])))
    
    else:
        print(f'#{i} ')
        print(' '.join(map(str, pascal[0])))
        print(' '.join(map(str, pascal[1])))

        for j in range(1, N-1):
            pascal_tmp = [1]

            for num in range(1, len(pascal)):
                pascal_tmp.append(pascal[j][num-1] + pascal[j][num])
            pascal_tmp.append(1)
            pascal.append(pascal_tmp)
            print(' '.join(map(str, pascal_tmp)))