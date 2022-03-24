dct = {'1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E':'1110', 'F': '1111', '0': '0000'}
code = {(1, 1, 2): 0,
        (1, 2, 2): 1,
        (2, 2, 1): 2,
        (1, 1, 4): 3,
        (2, 3, 1): 4,
        (1, 3, 2): 5,
        (4, 1, 1): 6,
        (2, 1, 3): 7,
        (3, 1, 2): 8,
        (2, 1, 1): 9}

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    numbers = []
    for _ in range(N):
        numbers.append(input().strip().strip('0'))
    
    binary = [''] * N
    for i in range(N):
        for j in range(len(numbers[i])):
            binary[i] += bin(int(numbers[i][j], base=16)).replace('0b', '').zfill(4)
        binary[i] = binary[i].zfill(4 * M).rstrip('0')
    tmp = []
    visited = []
    ans = 0
    
    for i in range(N):
        c1 = c2 = c3 = 0
        for j in range((M * 4) - 1, -1, -1):
            if c2 == 0 and c3 == 0 and binary[i][j] == '1':
                c1 += 1
            elif c1 > 0 and c3 == 0 and binary[i][j] == '0':
                c2 += 1
            elif c1 > 0 and c2 > 0 and binary[i][j] == '1':
                c3 += 1
            if c1 > 0 and c2 > 0 and c3 >0 and binary[i][j] == '0':
                c1 = c1 // min(c1, c2, c3)
                c2 = c2 // min(c1, c2, c3)
                c3 = c3 // min(c1, c2, c3)
                tmp.append(code[(c1, c2, c3)])
                c1 = c2 = c3 = 0
                
        if len(tmp) == 8:
            tmp2 = tmp[::-1]
            result = ((tmp2[0] + tmp2[2] + tmp2[4] + tmp2[6]) * 3) + (tmp2[1] + tmp2[3] + tmp2[5]) + tmp2[7]
            
            if result % 10 == 0 and tmp2 not in visited:
                ans += sum(tmp)
            visited.append(tmp2)
            tmp = []
        
    print(f'#{test_case} {ans}')