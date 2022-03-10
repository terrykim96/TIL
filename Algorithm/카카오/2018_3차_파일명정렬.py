def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''

        number_check = False
        for i in range(len(f)): # 문자열을 자른다.
            if f[i].isdigit():  # 처음 나오는 숫자부터는 NUMBER 부분이다.
                number += f[i]
                number_check = True
            elif not number_check:  # NUMBER가 나오기 전까지는 HEAD이다.
                head += f[i]
            else:               # NUMBER가 이미 나왔고, 숫자가 아닌 문자가 나오면 TAIL이다.
                tail = f[i:]
                break
        answer.append((head, number, tail))  # HEAD, NUMBER, TAIL을 하나의 튜플로 저장한다.

    answer.sort(key=lambda x: (x[0].upper(), int(x[1])))  # HEAD를 먼저 고려하고, NUMBER 다음으로 고려하여 정렬한다.
    
    ans = []
    for i in answer:            # 원래 형태로 문자열 만들어서 반환한다.
        ans.append(''.join(i))
        
    return ans