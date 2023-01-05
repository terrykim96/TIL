n = int(input())
ans = 0

for a in range(1, n):
    for b in range(a, n):
        c = n - (a + b)

        if c < b: continue
        
        if b + a > c:
            ans += 1

print(ans)