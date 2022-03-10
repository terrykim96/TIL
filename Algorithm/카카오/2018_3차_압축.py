def solution(msg):
    answer = []
    alpha_dict = {}
    
    for idx, value in enumerate(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')):    # 딕셔너리에 A: 1, B: 2 ...이렇게 담아준다.
        alpha_dict[value] = idx + 1
    
    i = 0           # 인덱싱 변수 i, 문자열 길이를 나타내는 length, 사전에 추가해줄 때 사용할 변수 cnt를 설정한다
    length = 0
    cnt = 26
    
    while True:
        length += 1     # 딕셔너리에 자료형이 존재하지 않는 문자열을 찾을 때까지 길이를 늘린다
        if not msg[i : i + length] in alpha_dict:   # 딕셔너리에 자료형이 존재하지 않는 문자열이 나오면
            answer.append(alpha_dict[msg[i : i + length - 1]])  # 그보다 작은 길이의 문자열에 해당하는 딕셔너리 자료형의 값을 추가한다.
            cnt += 1
            alpha_dict[msg[i : i + length]] = cnt   # 딕셔너리에 새로운 문자열을 추가한다.
            i += length - 1                         # 시작 위치와 문자열 길이를 바꿔준다.
            length = 0
        else:
            if (i + length - 1) == len(msg):        # 끝까지 봤을 때 딕셔너리에 자료형이 있다면 마지막으로 값을 추가하고 끝낸다.
                answer.append(alpha_dict[msg[i : i + length - 1]])
                break
    return answer