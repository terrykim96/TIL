#아래,오른쪽,위,왼쪽
dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt=2

start_x,start_y = start
maps[start_x][start_y] =1
stack = [(start_x,start_y)]
cur_x = cur_y = 0
while(True):
#print('while 처음',stack)
    while(stack):
        cur_x,cur_y = stack.pop()
        nx = cur_x +dx[dir]
        ny = cur_y +dy[dir]
        #print(nx,ny,cnt)
        if(nx>=r or nx<0 or ny>=c or ny<0):
            continue
        if(maps[nx][ny]!=0):
            continue
        maps[nx][ny]=cnt
        if (cnt == k):
            print(nx + 1, ny + 1)
        stack.append((nx,ny))
        cnt+=1

    stack.append((cur_x,cur_y))
    #print('막혀부렷어 다시 넣어',stack)
    if(dir==0):
        dir = 1
    elif(dir==1):
        dir = 2
    elif(dir==2):
        dir =3
    else:
        dir =0