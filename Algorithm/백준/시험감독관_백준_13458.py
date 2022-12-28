N = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

ans = N

for i in range(N):
    if students[i] <= b:
        continue
    
    else:
        if (students[i] - b) % c != 0:
            ans += ((students[i] - b) // c + 1)
        
        else:
            ans += ((students[i] - b) // c)
            
print(ans)