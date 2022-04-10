N = int(input())
M = int(input())
edge = []
parent = {}
rank = {}
ans = 0

# 부모를 찾는 함수
def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]

# 합치는 함수(grouping)
def union(v1, v2):
    root1 = find(v1)
    root2 = find(v2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        
        if rank[root1] == rank[root2]:
            rank[root2] += 1

for i in range(1, N + 1):       # 부모를 찾아준다.
    parent[i] = i
    rank[i] = 0

for i in range(M):
    a, b, c = map(int, input().split())
    edge.append((c, a, b))
edge.sort()

for e in edge:  # edge를 순회하면서
    w, v, u = e

    if find(v) != find(u):  # a 컴퓨터와 b 컴퓨터의 루트 노드가 다르다면 사이클을 이루지 않기 때문에 union으로 합쳐준다.
        union(v, u)
        ans += w

print(ans)