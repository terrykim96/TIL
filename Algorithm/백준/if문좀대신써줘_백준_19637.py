import sys
input = sys.stdin.readline

N, M = map(int, input().split())
power_list = []
name_list = []

for i in range(N):
    name, power = input().split()
    power = int(power)

    if power_list and power_list[-1] == power:  # 가장 처음 칭호만 지정한다.
        continue

    power_list.append(power)
    name_list.append(name)

def binary_search(power):       # 이분 탐색으로 칭호를 찾아서 출력한다.
    left = 0
    right = len(power_list) - 1

    while left <= right:
        mid = (left + right) // 2

        if power > power_list[mid]:
            left = mid + 1

        else:
            right = mid - 1

    print(name_list[right + 1])

for _ in range(M):
    power = int(input())

    binary_search(power)