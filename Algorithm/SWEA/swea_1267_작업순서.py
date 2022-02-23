T = 10

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    adj = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    cnt = V
    tmp_lst = list(map(int, input().split()))   # 입력값을 받기 힘들어서 한번 받은 뒤에 반복문으로 adj에 넣어준다.
    
    for i in range(0, len(tmp_lst), 2):         # 선행 작업이 되어야 다음 작업이 가능하므로 순서를 반대로 받아준다.
        adj[tmp_lst[i + 1]].append(tmp_lst[i])  # tmp_lst[i]가 1이고 tmp_lst[i + 1]이 2라면 2번 작업은 1번 작업이 수행완료일 때만 수행 가능하다.

    ans = []

    while cnt:  # 모든 작업을 돌아보기 위해 cnt를 총 작업 갯수에서부터 1씩 줄이면서 진행한다.
        for i in range(1, V+1):
            if not visited[i]:  # 작업이 수행되지 않았을 때
                for j in adj[i]:    # 선행 작업이 수행되지 않았다면 break해준다.
                    if not visited[j]:
                        break
                else:           # break 되지 않았다면 방문 리스트에 업데이트 하고 정답 리스트에 append해준다.
                    visited[i] = 1
                    ans.append(i)
                    cnt -= 1    # cnt도 줄여준다.
    
    print(f'#{test_case}', *ans)