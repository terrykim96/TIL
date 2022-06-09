import sys
sys.setrecursionlimit(100000000)         # 재귀 깊이 제한을 늘려준다.

input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]  # 자기 자신을 부모로 갖는 n + 1개 집합을 만들어준다.


def find_parent(x):                 # 찾기 연산(같은 집합에 속하는지 확인하기 위한 함수)를 정의한다.
    if parent[x] != x:              # 두 원소가 같은 부모 원소를 가지지 않으면
        parent[x] = find_parent(parent[x])  # 재귀로 같은 부모 원소를 가지는 둘을 찾아준다.

    return parent[x]


def union_parent(a, b):             # 합집합 연산(두 집합을 합치기 위한 함수)를 정의한다.
    a = find_parent(a)
    b = find_parent(b)
    
    if a < b:                       # 값이 더 작은 쪽을 부모로 한다.
        parent[b] = a
    else:
        parent[a] = b

for _ in range(m):
    do, a, b = map(int, input().split())
    if do == 0:
        union_parent(a, b)
        
    else:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")