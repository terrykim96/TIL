def solution(n, t, m, timetable):
    ans = 0

    # 모든 시간을 분으로 환산해서 생각한다.
    # 09:10 -> 9*60 + 10 = 550(분)

    crew = [int(time[:2])*60 + int(time[3:]) for time in timetable]     # 크루 도착 시각 리스트
    crew.sort()

    bus = []
    for i in range(n):  # 버스 도착 시각 리스트
        bus.append(9*60 + t*i)

    i = 0               # 다음 버스에 오를 크루 인덱스를 지정해준다.

    for tm in bus:      # 버스 도착 시간에 대해
        cnt = 0         # 버스에 타는 크루 수이다.
        while cnt < m and i < len(crew) and crew[i] <= tm:  # 버스에 자리가 남아있고, 탑승할 크루가 남아있고, 해당 크루가 버스 도착 시간 전에 도착했다면, 버스에 타는 크루 수를 계산하고 다음 크루로 넘긴다.
            i += 1
            cnt += 1
        
        if cnt < m:     # 버스에 자리가 남았을 경우
            ans = tm

        else:           # 버스에 자리가 없는 경우 맨 마지막 크루보다 1분 먼저 도착한다.
            ans = crew[i - 1] - 1

        answer = str(ans//60).zfill(2) + ':' + str(ans%60).zfill(2) # 출력 형식에 맞게 지정해준다.
    
    return answer