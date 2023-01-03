M = int(input())

ans = 1
rot = 0

for i in range(M) :
    first, second, dir = map(int, input().split())
    
    ans = ans * second / first    # 바퀴의 회전수는 (전 바퀴의 회전 수 * 두번째 바퀴 / 첫번째 바퀴)이다.
    
    if dir:         # 꼬였으면 방향을 바꿔준다.
        rot = not rot
        

print(rot*1, int(ans))