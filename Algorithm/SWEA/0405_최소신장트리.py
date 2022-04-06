def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    parent[y] = x

T = int(input())

for test_case in range(1, T + 1):
    v, e = map(int, input().split())  # 마지막 노드 번호, 간선 수
    graph = []
    ans = 0
    
    parent = [i for i in range(v + 1)]
    for _ in range(e):
        n1, n2, w = map(int, input().split())
        graph.append((n1, n2, w))

    graph.sort(key=lambda x: x[2])
    cnt = 0
    
    for n1, n2, w in graph:
        if find(n1) != find(n2):
            union(n1, n2)
            ans += w
            cnt += 1
        if cnt == v:
            break
            
    print(f'#{test_case} {ans}')