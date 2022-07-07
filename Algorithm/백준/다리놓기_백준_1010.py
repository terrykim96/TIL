from math import factorial

# Combination
T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    print(int(factorial(M) / (factorial(N) * factorial(M - N))))