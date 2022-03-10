def solution(m, musicinfos):
    answer = '(None)'       # 답을 찾지 못하면 (None)을 반환해야 하므로 초기값을 설정한다.
    max_time = 0
    # replace로 #들을 새로운 글자로 치환해준다.
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    
    for music in musicinfos:
        start, end, title, melody = music.split(',')
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        time = 60*(end_h-start_h) + (end_m-start_m)     # 시간을 분으로 바꿔준다.

        # replace로 #들을 새로운 글자로 치환해준다.
        melody = melody.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
        played = (melody * time)[:time]         # 실제로 재생된 멜로디를 저장한다.
        
        if m in played and time > max_time:     # 겹치는 음이 있으면서 길이가 가장 긴 음악을 찾는다.
            
            answer = title
            max_time = time
        
    return answer