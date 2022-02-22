def check(lst):
    target = {'}':'{', ')':'('}
    stack = []

    for i in lst:
        if i in ('{', '('):
            stack.append(i)
        elif i in ('}', ')'):
            if len(stack) == 0 or stack[-1] != target[i]:
                return 0
            else:
                stack.pop()
    if stack:
        return 0
    else:
        return 1
    
T = int(input())

for tc in range(1, T + 1):
    string = input()
    print(f'#{tc} {check(string)}')