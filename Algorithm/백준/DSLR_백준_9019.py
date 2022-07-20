from collections import deque
import sys

input = sys.stdin.readline
    

T = int(input())

for _ in range(T):

    A, B = map(int, input().split())
    arr = [0] * 10000

    q = deque()
    q.append([A, ""])

    while q:
        number, result = q.popleft()
        
        dn = (number * 2) % 10000

        if dn == B:
            print(result + "D")

        elif arr[dn] == 0:
            arr[dn] = 1

            q.append([dn, result + "D"])

        if number != 0:
            sn = number - 1

        else:
            sn = 9999

        if sn == B:
            print(result + "S")

        elif arr[sn] == 0:
            arr[sn] = 1

            q.append([sn, result + "S"])

        ln = int(number % 1000 * 10 + number / 1000)

        if ln == B:
            print(result + "L")

        elif arr[ln] == 0:
            arr[ln] = 1

            q.append([ln, result + "L"])

        rn = int(number % 10 * 1000 + number // 10)

        if rn == B:
            print(result + "R")

        elif arr[rn] == 0:
            arr[rn] = 1

            q.append([rn, result + "R"])