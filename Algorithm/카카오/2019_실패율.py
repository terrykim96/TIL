def solution(N, stages):
    solve = len(stages)
    lst = []

    for i in range(1, N + 1):   # 각 스테이지마다
        tmp = 0
        for j in range(len(stages)):    # 스테이지 실패율을 lst에 append한다.
            if stages[j] == i:          # tmp는 도달했지만 클리어하지 못한 플레이어 수, solve는 스테이지에 도달한 플레이어 수 
                tmp += 1
        if tmp == 0:
            lst.append(0)
        else:
            lst.append(tmp / solve)
        solve = solve - tmp             # 다음 스테이지

    sort_lst = sorted(lst, reverse= True)   # 스테이지 실패율 내림차순
    answer = []

    for i in range(len(lst)):           # 실패율이 높은 스테이지의 index를 answer에 담아준다.
        answer.append(lst.index(sort_lst[i]) + 1)
        lst[lst.index(sort_lst[i])] = 999   # 중복 방지를 위해 999로 설정
    
    return answer