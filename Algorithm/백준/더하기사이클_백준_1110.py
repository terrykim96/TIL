num = int(input())
check = num
new_num = 0
tmp = 0
ans = 0

while True:
    tmp = num // 10 + num % 10
    new_num = (num % 10) * 10 + tmp % 10
    ans += 1
    num = new_num

    if new_num == check:
        break

print(ans)