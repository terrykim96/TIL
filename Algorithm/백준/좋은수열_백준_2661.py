def good_bad(number, depth):
    for i in range(depth):
        tmp = number[i:]
        for j in range(1, len(tmp) // 2 + 1):
            check = tmp[:j]
            if check == tmp[j: j + 1]:
                return False
    return True

def dfs(depth):
    if not good_bad(number, depth):
        return -1
    
    if depth == N:
        print(''.join(number))
        return 0
    
    for i in range(1, 4):
        number.append(str(i))

        if dfs(depth + 1) == 0:
            return 0
        number.pop()

N = int(input())
number = []
dfs(0)