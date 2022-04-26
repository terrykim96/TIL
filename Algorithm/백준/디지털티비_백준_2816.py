N = int(input())
channel = []

for i in range(N):
    name = input()
    
    if name == 'KBS1':
        idx1 = i
    elif name == 'KBS2':
        idx2 = i
    channel.append(name)

ans = ''
ans += '1' * idx1       # kbs1이 있는 곳으로 1번을 이용해 화살표를 내린다.
ans += '4' * idx1       # kbs1을 4번을 이용해 첫번째로 보낸다.

if idx1 > idx2:         # kbs1이 kbs2보다 아래에 있으면 kbs1을 첫번째로 보내는 과정을 통해 kbs2의 위치가 하나 낮아졌다. (index는 1 증가한다.)
    idx2 += 1

ans += '1' * idx2       # kbs2가 있는 곳으로 1번을 화살표를 내린다.
ans += '4' * (idx2 - 1) # kbs2를 4번을 이용해서 두 번째로 보낸다. (첫번째가 아닌 두번째로 이동하면 되니까 idx2 - 1 만큼 실행한다.)

print(ans)