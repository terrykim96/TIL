import sys

N, M = map(int, sys.stdin.readline().split())
board = dict()

for _ in range(N) :     # 딕셔너리 구조로 키워드를 저장한다.
    keyword = sys.stdin.readline().rstrip()
    board[keyword] = 1
    
ans = N
for _ in range(M) :
    posts = sys.stdin.readline().rstrip().split(',')
    posts.sort()
    
    for word in posts :     # 가희가 글을 쓰면 키워드에서 하나씩 지운다.
        if word in board.keys() :
            if board[word] == 1 :
                board[word] -= 1
                ans -= 1

    print(ans)