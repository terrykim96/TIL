plus = [0] * 1000001
plus[0] = plus[1] = 1
plus[2] = 2

for i in range(3, 1000001):
    plus[i] = (plus[i - 3] + plus[i - 2] + plus[i - 1]) % 1000000009

T = int(input())

for _ in range(T):
    N = int(input())    
    print(plus[N] % 1000000009)