import sys
sys.setrecursionlimit(2000) #최대 재귀를 늘려준다.

input = sys.stdin.readline

def dfs(x):
    visited[x] = 1          # 방문을 체크한다.
    number = numbers[x]     # 다음 방문 장소를 방문하지 않았다면
    if not visited[number]: # 재귀에 넣는다.
        dfs(number)

for _ in range(int(input())):
    N = int(input())
    numbers = [0] + list(map(int, input().split()))
    visited = [1] + [0] * N  # 방문 여부를 확인할 배열
    ans = 0
    
    for i in range(1, N + 1):
        if not visited[i]:          # 방문하지 않았다면 dfs를 실행한다.
            dfs(i)                  
            ans += 1             # 결과값에 1을 더해준다.
    
    print(ans)