def solution(record):
    answer = []
    dic = {}
    
    for sentence in record:     # 처음에 inout, uid, name으로 하려했는데 Leave일 때는 map으로 2개가 나와서 그냥 tuple로 받음
        sentence_split = sentence.split()
        if len(sentence_split) == 3:    # Enter나 Change면 딕셔너리에 value값으로 저장한다.
            dic[sentence_split[1]] = sentence_split[2]
            
    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append(f'{dic[sentence_split[1]]}님이 들어왔습니다.')
        elif sentence_split[0] == 'Leave':
            answer.append(f'{dic[sentence_split[1]]}님이 나갔습니다.')
            
    return(answer)