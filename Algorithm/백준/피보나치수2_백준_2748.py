n = int(input())

# 시간초과
# def fibonacci(num):
#     if num == 0:
#         return 0
    
#     elif num <= 2:
#         return 1
    
#     return fibonacci(num - 2) + fibonacci(num - 1)

# print(fibonacci(n))

fibonacci = []
num = 0

for i in range(n + 1):
    if i == 0:
        num = 0

    elif i <= 2:
        num = 1
        
    else:
        num = fibonacci[-1] + fibonacci[-2]
    
    fibonacci.append(num)

print(fibonacci[-1])