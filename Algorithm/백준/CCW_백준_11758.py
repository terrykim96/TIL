x1, y1 =map(int,input().split())
x2, y2=map(int,input().split())
x3, y3=map(int,input().split())

if x2 - x1 == 0:
    if x3 - x2 == 0:
        print(0)

    else:
        if (x3 - x2)*(y2 - y1) < 0:
            print(1)
        else:
            print(-1)

else:
    if x3 - x2 == 0:
        if (x2  -x1)*(y3 - y2) > 0:
            print(1)

        else:
            print(-1)

    else:
        p = (y2 - y1) / (x2 - x1)
        k = y3 - p * (x3 - x1) - y1

        if p == (y3 - y2) / (x3 - x2):
            print(0)

        elif x2 - x1 > 0:
            if k > 0:
                print(1)
            else:
                print(-1)

        else:
            if k > 0:
                print(-1)
            else:
                print(1)