def solution(dartResult):
    n = ''
    ans = []

    # 그냥 모든 경우에 대해 다 구해준다.
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            n = int(n)**1
            ans.append(n)
            n = ''
        elif i == 'D':
            n = int(n)**2
            ans.append(n)
            n = ''
        elif i == 'T':
            n = int(n)**3
            ans.append(n)
            n = ''
        elif i == '*':
            if len(ans) > 1:
                ans[-2] = ans[-2] * 2
                ans[-1] = ans[-1] * 2
            else:
                ans[-1] = ans[-1] * 2
        elif i == '#':
            ans[-1] = ans[-1] * -1
        
    return sum(ans)