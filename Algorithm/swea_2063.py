from statistics import median


numbers = list(map(int, input().split(" ")))

ans = median(numbers)

print(ans)