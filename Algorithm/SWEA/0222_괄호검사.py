def check(lst):
    target = {'}':'{', ')':'('}
    stack = []

    for i in lst:
        if i in ('{', '('):
            stack.append(i)
        elif i in ('}', ')'):
            if stack[-1] != target[i] or len(stack) == 0:
                return 0
            stack.pop()
    if stack:
        return 0
    else:
        return 1
    
T = int(input())

for test_case in range(1, T + 1):
    print(f'#{test_case} {check(input())}')