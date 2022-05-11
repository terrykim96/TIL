N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

S = 0
for _ in range(N):
    S += A[0] * max(B)
    A.pop(0)
    B.pop(B.index(max(B)))

print(S)