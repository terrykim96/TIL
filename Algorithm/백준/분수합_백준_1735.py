import math

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

# 통분하여 더해준다.
top = a1 * b2 + a2 * b1
bottom = b1 * b2

# 분자와 분모의 최대공약수를 구해서 나눠준다
gcd = math.gcd(top, bottom)
top //= gcd
bottom //= gcd

print(top, bottom)