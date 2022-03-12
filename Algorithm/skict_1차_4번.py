'''
n개의 노드로 이루어진 트리가 있습니다. 각 노드에는 0번부터 n-1번까지 번호가 매겨져 있습니다. 이때, 당신은 다음 조건을 모두 만족하는 정수 순서쌍 (i,j,k)의 개수를 구하고자 합니다.

0 ≤ i, j, k < n
i, j, k는 서로 다릅니다.
distance(a, b)를 a번 노드와 b번 노드를 잇는 경로 상의 간선의 개수라고 할 때, distance(i, j) + distance(j, k) = distance(i, k)입니다.
트리의 노드 개수를 의미하는 n과 간선 정보가 담긴 2차원 정수 배열 edges가 매개변수로 주어집니다. 주어진 조건을 모두 만족하는 순서쌍 (i,j,k)의 개수를 return 하도록 solution 함수를 완성해주세요.
'''


tmp = 10e16

def solution(n, edges):
    answer = 0
    tree = [[tmp]*n for _ in range(n)]
    for edge in edges:
        tree[edge[0]][edge[1]] = 1
        tree[edge[1]][edge[0]] = 1
    for k in range(n):
        tree[k][k] = 0
        for i in range(n):
            for j in range(n):
                tree[i][j] = min(tree[i][j], (tree[i][k]+tree[k][j]))
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i != j != k and (tree[i][j] + tree[j][k]) == tree[i][k]:
                    answer += 1
    return answer
