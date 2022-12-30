N = int(input())

ans = []

for _ in range(N):
    name, day, month, year = input().split()
    day, month, year = map(int,(day, month, year))      # 생년월일을 숫자로 바꾸고, yyyymmdd 순서로 바꿔서 리스트에 저장한다.
    ans.append((year, month, day, name))            # [(1999, 12, 23, 이름), (1998, 12, 23, 이름2), (1999, 10, 24, 이름)]

ans.sort()          # sort하면 요소 순서대로 정렬된다.

print(ans[-1][3])   # 가장 나이 적은 사람(마지막 원소)
print(ans[0][3])    # 가장 나이 많은 사람(첫번째 원소)