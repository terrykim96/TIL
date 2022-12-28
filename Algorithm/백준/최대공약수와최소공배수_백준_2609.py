a, b = map(int, input().split())

def gcd(a, b):      # 최대공약수
    tmp = min(a, b)

    for i in range(tmp, 0, -1):     # 두 숫자를 나눴을 때 다 나머지가 0인 애들 중 가장 큰애
        if not a % i and not b % i:
            return i

def lcm(a, b):      # 최소공배수
    return a * b // gcd(a, b)       # 유클리드 호제법 (최대공약수로 두 수 곱한거 나누기)

print(gcd(a, b))
print(lcm(a, b))

# math 사용해서 하기
import math

print(math.gcd(a, b))
print(math.lcm(a, b))