T = int(input())

for test_case in range(1, T + 1):
    tokens =list(input().split())
    stk = []
    
    for i in range(len(tokens) -1):
        if tokens[i].isdigit():
            stk.append(tokens[i])
        else: 
            try:
                b, a = int(stk.pop()), int(stk.pop())
                if tokens[i] == '+':
                    c = a + b
                elif tokens[i] == '-':
                    c = a - b
                elif tokens[i] == '/':
                    c = a // b
                elif tokens[i] == '*':
                    c = a * b
                stk.append(str(c))
            except:
                ans = 'error'

    if len(stk) == 1:
        ans = stk.pop()
    else:
        ans = 'error'

    print(f'#{test_case} {ans}')