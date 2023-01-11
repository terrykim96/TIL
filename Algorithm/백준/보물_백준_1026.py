N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()

S = 0
for _ in range(N):
    S += A[0] * max(B)  # 큰 수끼리 곱하고 작은 수끼리 곱해야한다.
    A.pop(0)
    B.pop(B.index(max(B)))

print(S)