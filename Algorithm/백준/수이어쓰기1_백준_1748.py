N = input()
tmp = len(N) - 1
ans = 0

for i in range(tmp):
    ans += 9 * (10 ** i) * (i + 1)

ans += (int(N) - (10 ** tmp) + 1) * (tmp + 1)

print(ans)