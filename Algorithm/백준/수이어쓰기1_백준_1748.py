N = input()
tmp = len(N) - 1    # 입력 받은 수의 자릿수를 구한다.
ans = 0

for i in range(tmp):    # (자릿수 - 1)까지 공식으로 구한다.
    ans += 9 * (10 ** i) * (i + 1)

ans += (int(N) - (10 ** tmp) + 1) * (tmp + 1)   # 입력 받은 숫자의 자릿수 부터는 그 숫자 갯수만큼 더한다.

print(ans)