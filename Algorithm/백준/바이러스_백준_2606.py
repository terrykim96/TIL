n = int(input())
m = int(input())
graph = [[]*n for _ in range(n+1)]

for _ in range(m):      # 간선 정보를 graph에 저장한다.
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
cnt = 0
visited = [0]*(n+1)

def dfs(start):         # dfs를 재귀로 구현한다.
    global cnt
    visited[start] = 1
    for i in graph[start]:  # 연결된 지점을 방문하지 않았다면 거기서 dfs 함수를 재귀적으로 실행한다.
        if visited[i]==0:
            dfs(i)
            cnt +=1
 
dfs(1)
print(cnt)