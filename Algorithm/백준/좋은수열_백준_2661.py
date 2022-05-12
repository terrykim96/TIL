def good_bad(number, depth):        # 좋은 수열인지 나쁜수열인지 파악해주는 함수이다.
    for i in range(depth):
        tmp = number[i:]
        for j in range(1, len(tmp) // 2 + 1):
            check = tmp[:j]
            if check == tmp[j: 2*j]:
                return False
    return True

def dfs(depth):                     # 백트래킹을 활용한 DFS로 찾아준다.
    if not good_bad(number, depth): # 나쁜 순열이면 즉시 종료한다.
        return -1
    
    if depth == N:                  # 깊이가 N이 되면(길이가 N개가 되면) print해준다.
        for i in range(N):
            print(number[i], end= '')
        return 0
    
    for i in range(1, 4):           # 1에서부터 순서대로 넣기 때문에 최소값을 구할 수 있다.
        number.append(i)

        if dfs(depth + 1) == 0:
            return 0
        number.pop()

N = int(input())
number = []
dfs(0)