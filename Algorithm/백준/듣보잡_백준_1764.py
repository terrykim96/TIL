N, M = map(int, input().split())

listen = []
see = []

for _ in range(N):
    listen.append(input())

for _ in range(M):
    see.append(input())

listen_see = sorted(list(set(listen) & set(see)))       # 교집합으로 듣보잡을 구해준다.


print(len(listen_see))
for person in listen_see:
    print(person)