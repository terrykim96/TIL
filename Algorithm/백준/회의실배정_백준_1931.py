N = int(input())
meeting = []

for _ in range(N):
    start, end = map(int, input().split())  # [시작시간, 끝나는 시간]의 형태로 저장한다.
    meeting.append([start, end])

meeting = sorted(meeting, key=lambda a: a[0])   # 시작 시간을 기준으로 먼저 정렬하고
meeting = sorted(meeting, key=lambda a: a[1])   # 끝나는 시간을 한 번 더 정렬해준다.

tmp = 0
ans = 0

for start, end in meeting:
    if start >= tmp:    # 끝나는 시간보다 시작 시간이 늦으면
        ans += 1        # 회의실에 더하고
        tmp = end       # 새롭게 끝나는 시간을 지정해준다.

print(ans)