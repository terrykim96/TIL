def is_round(string):
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return False
    return True

for _ in range(10):
    test_case = int(input())
    lst = [list(input()) for _ in range(100)]
    lst2 = list(zip(*lst))
    ans = 1
    
    for leng in range(100, 1, -1):
        if ans >= leng:
            break
        for i in range(100):
            if ans == leng:
                break
            for j in range(100 - leng + 1):
                if is_round(lst[i][j : j + leng]) or is_round(lst2[i][j : j  + leng]):
                    ans = leng
                    break
    
    print(f'#{test_case} {ans}')