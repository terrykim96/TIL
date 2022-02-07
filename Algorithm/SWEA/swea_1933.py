num = int(input())

for i in range(num+1):
    if num % i == 0:
        print(i, end= ' ')