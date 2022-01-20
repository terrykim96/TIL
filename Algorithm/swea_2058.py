numbers = input()
ans = 0
for i in range(len(numbers)):
    ans += int(numbers[i])

print(ans)

# 재귀로
def sum_of_digit_recursive(numbers):
    if len(str(numbers)) == 1:
        return numbers
    
    return int(str(numbers)[0]) + sum_of_digit_recursive(int(str(numbers)[1:]))