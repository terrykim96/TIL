def check(s, leng):
    for i in range(leng):
        if src[s + i] != target[i]:
            return False
    return True

for test_case in range(1, 11):
    _ = input()
    target = input()
    src = input()
    ans = 0

    for i in range(len(src) - len(target) + 1):
        if check(i, len(target)):
            ans += 1
    print(f'#{test_case} {ans}')
    