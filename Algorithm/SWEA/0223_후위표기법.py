T = int(input())

for test_case in range(1, T + 1):
    tokens =list(map(str,input())) 
    lst = []
    stk = []
    prior = {'*':3,'/':3,'+':2,'-':2,'(':1}     # 우선순위 설정
    for n in range(len(tokens)):    # 토큰의 길이만큼 반복하여
        if tokens[n].isdigit(): # 만약 숫자이면 바로 lst에 추가
            lst.append(tokens[n])
        elif tokens[n] == '(':  # (이면 바로 stack에 추가
                stk.append(tokens[n])
        elif tokens[n] == ')':  # )가 나오면 stack에서 (가 나올때까지 pop처리 및 lst에 추가. 
            while stk[-1] != '(':
                lst.append(stk.pop())
            stk.pop() # (가 나타나면 pop처리
        else:   # 그외에 경우 tokens[n]이 stack[-1]의 우선순위와 같거나 보다 작으면 tokens[n]의 우선순위가 더 커질때까지 pop
            while stk and prior[tokens[n]] <= prior[stk[-1]]:
                lst.append(stk.pop()) # pop한것들은 lst에 추가 시켜줌   
            stk.append(tokens[n]) # 위의 조건이 완료 되면 stack에 추가

    while len(stk) != 0:  # stack에 남아있는 연산자들 lst에 추가
        lst.append(stk.pop())

    print(f'#{test_case}', ''.join(lst))