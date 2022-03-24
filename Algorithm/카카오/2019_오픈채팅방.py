def solution(record):
    answer = []
    dic = {}
    
    for sentence in record:     # 처음에 inout, id, name으로 하려했는데 Leave일 때는 map으로 2개가 나와서 실패
        sentence_split = sentence.split()
        if len(sentence_split) == 3:
            dic[sentence_split[1]] = sentence_split[2]
            
    for sentence in record:
        sentence_split = sentence.split()
        if sentence_split[0] == 'Enter':
            answer.append(f'{dic[sentence_split[1]]}님이 들어왔습니다.')
        elif sentence_split[0] == 'Leave':
            answer.append(f'{dic[sentence_split[1]]}님이 나갔습니다.')
            
    return(answer)