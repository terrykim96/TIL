A, P = map(int, input().split())

D = [A]

while True:
    tmp = 0

    for i in str(D[-1]):        # 각 자리 숫자를 추출해서 P제곱 해주고 더해준다.
        tmp += int(i) ** P

    if tmp in D:                # 반복되는 수가 있으면 끝낸다.
        break

    D.append(tmp)

print(D.index(tmp))             # while문이 끝났을 때, 마지막으로 남은 tmp가 반복되는 주기이다.