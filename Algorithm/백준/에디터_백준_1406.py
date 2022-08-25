import sys

input = sys.stdin.readline

stk1 = list(input().strip())
stk2 = []
M = int(input())

for _ in range(M):
    order = input().strip().split(' ')

    if order[0] == 'L':
        if stk1: stk2.append(stk1.pop())
        
    elif order[0] == 'D':
        if stk2: stk1.append(stk2.pop())
        
    elif order[0] == 'B':
        if stk1: stk1.pop()
        
    elif order[0] == 'P':
        stk1.append(order[1])

print(''.join(stk1 + list(reversed(stk2))))