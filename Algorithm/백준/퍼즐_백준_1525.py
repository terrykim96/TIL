import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


start = ""
for _ in range(3):
    temp = sys.stdin.readline().strip()
    temp = temp.replace(" ", "")
    start += temp

start = start.replace("0", "9")

q = deque()
q.append(start)

cntDict = dict()
cntDict[start] = 0


while q:
    now = q.popleft()
    
    if now == "123456789":
        break