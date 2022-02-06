N = int(input())

student_num = list(map(int, input().split()))
ans = []

for i in range(N):
    ans.insert(i - student_num[i], i + 1)

print(*ans)