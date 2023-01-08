import sys
sys.setrecursionlimit(10**9)    # 재귀 제한 늘려준다.

nums = []

while True:
    try:
        nums.append(int(input()))

    except:
        break
        
def pre_order(s, e):
    if s > e:
        return

    mid = e + 1                         # 오른쪽 노드가 없을 경우

    for i in range(s + 1, e + 1):
        if nums[s] < nums[i]:
            mid = i

            break

    pre_order(s + 1, mid - 1)               # 왼쪽 확인
    pre_order(mid, e)                   # 오른쪽 확인

    print(nums[s])

pre_order(0, len(nums) - 1)