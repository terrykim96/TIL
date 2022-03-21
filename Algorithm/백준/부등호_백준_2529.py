n = int(input())
op = input().split()
visited = [0] * 10
mx, mn = "", ""

def possible(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True

def dfs(cnt, s):
    global mx, mn
    if cnt == n + 1:
        if not len(mn):
            mn = s
        else:
            mx = s
        return
    for i in range(10):
        if not visited[i]:
            if cnt == 0 or possible(s[-1], str(i), op[cnt - 1]):
                visited[i] = 1
                dfs(cnt + 1, s + str(i))
                visited[i] = 0
dfs(0, "")
print(mx)
print(mn)