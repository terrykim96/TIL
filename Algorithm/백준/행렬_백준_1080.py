N, M = map(int, input().split())

A = []
for _ in range(N):
    A.append(list(map(int, list(input()))))

B = []
for _ in range(N):
    B.append(list(map(int, list(input()))))


def flip(i, j): # 뒤집기 함수
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            if A[x][y] == 0:
                A[x][y] = 1
            else:
                A[x][y] = 0


cnt = 0
if (N < 3 or M < 3) and A != B: # 리스트가 3x3보다 작으면서 A와 B가 다를 때는 불가능하다.
    cnt = -1
else:
    for i in range(N - 2):
        for j in range(M - 2):  # 모든 점에 대해 두개를 비교하여 다르면 flip 실행
            if A[i][j] != B[i][j]:
                cnt += 1
                flip(i, j)

if cnt != -1:
    if A != B: # 다 뒤집고 나서 A와 B가 같은지 확인해서 다르면 -1이다.
        cnt = -1

print(cnt)