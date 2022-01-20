password, start_num = map(int, input().split())

ans = 0
if password >= start_num:
    ans = password - start_num + 1
else:
    ans = 999 - start_num + 1 + password + 1

print(ans)