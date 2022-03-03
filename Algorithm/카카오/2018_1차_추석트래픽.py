def throughput(log, start, end):
    cnt = 0
    for i in log:
        if i[0] < end and i[1] >= start:
            cnt += 1
    return cnt


def solution(lines):
    ans = 0
    work = []                            # work에[시작시간, 끝시간] 저장
    for line in lines:
        date, s, t = line.split()       # 날짜, 응답완료시간, 처리시간
        s = s.split(':')
        t = t.replace('s', '')

        end = (int(s[0])*3600 + int(s[1])*60 + float(s[2])) * 1000 # 끝난 시간을 ms 단위로 저장
        start = end - float(t)*1000 + 1 # 시작 시간을 ms 단위로 저장
        work.append([start, end])
    for i in work:                       # 최대 초당 처리량 구하기
        ans = max(ans, throughput(work, i[0], i[0] + 1000), throughput(work, i[1], i[1] + 1000))

    return ans
