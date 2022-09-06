def solution(queue1, queue2):
    q_1 = sum(queue1)
    q_2 = sum(queue2)
    q_sum = (q_1 + q_2) // 2
    
    if (q_1 + q_2) % 2 == 1:
        return -1
    
    i = j = 0
    length = len(queue1)
    answer = -1
    
    
    while i < length * 2 and j < length * 2 and q_1 != q_2:
        if q_1 < q_sum:
            q_1 += queue2[j]
            q_2 -= queue2[j]
            
            queue1.append(queue2[j])
            j += 1
        else:
            q_2 += queue1[i]
            q_1 -= queue1[i]
            
            queue2.append(queue1[i])
            i += 1
        
    if q_1 == q_sum:
        answer = i + j
    
    return answer