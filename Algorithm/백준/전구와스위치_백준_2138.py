def zeroClick(state):               # 첫번째를 누르는 경우
    cnt=1
    state[0]=int(not state[0])      # 0과 1은 not으로 바꿀 수 있다.
    state[1] = int(not state[1])
    
    for i in range(1, N):
        if(state[i - 1] != result[i - 1]):
            cnt += 1
            state[i - 1] = int(not state[i - 1])
            state[i] = int(not state[i])
            
            if(i != N-1):
                state[i + 1]=int(not state[i + 1])
    
    if(state == result):
        return cnt
    else:                           # 불가능하면 -1 반환
        return -1


def zeroNoClick(state):             # 첫번째를 안누르는 경우
    cnt=0
    for i in range(1, N):
        if(state[i - 1] != result[i - 1]):
            cnt += 1
            state[i - 1]=int(not state[i - 1])
            state[i]=int(not state[i])
            if(i != N - 1):
                state[i + 1]=int(not state[i + 1])
    if(state==result):
        return cnt
    else:
        return -1


N = int(input())
state = list(map(int, input()))
result = list(map(int, input()))
cnt1 = zeroClick(state[:])      # 첫번째 전구를 누르는 경우와 안누르는 경우를 나누어 계산한다. 
cnt2 = zeroNoClick(state[:])

if cnt1 >= 0 and cnt2 >= 0:    # 불가능한 경우를 빼고 더 작은 경우 출력
    ans = min(cnt1, cnt2)
elif cnt1 >= 0 and cnt2 < 0:
    ans = cnt1
elif cnt1 < 0 and cnt2 >= 0:
    ans = cnt2
else:
    ans = -1

print(ans)