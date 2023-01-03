def get_clock_num(number):      # 시계수 구하는 함수를 만든다.
    clock_number = number

    for _ in range(3):
        number = (number & 1000) * 10 + number // 1000

        if clock_number > number:
            clock_number = number

    return clock_number

clock_num = get_clock_num(int(''.join(input().split())))

i = 1111
cnt = 0

while i <= clock_num:       # 1111부터 시작해서 순서를 구해준다.
    if get_clock_num(i) == i:
        cnt += 1

    i += 1

print(cnt)