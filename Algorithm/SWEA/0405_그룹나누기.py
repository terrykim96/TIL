def find(x):
    if parent[x] != x: parent[x] = find(parent[x])
    return parent[x]
 
def union(x, y):
    a = find(x)
    b = find(y)
    if a > b: parent[a] = b
    else: parent[b] = a

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    parent = [i for i in range(N+1)]
    votes = list(map(int, input().split()))
    for i in range(0, M*2, 2): union(votes[i], votes[i+1])
    
    ans = set()

    for i in parent:
        ans.add(find(i))
        
    ans = len(ans) - 1
    print(f'#{test_case} {ans}')