from itertools import combinations

L, C = map(int, input().split())
chars = input().split()        
aeiou = ['a', 'e', 'i', 'o', 'u']

ans = []

for tmp in list(combinations(chars, L)):    # L개로 구성된 암호 모두 만들기
    aeiou_cnt = else_cnt = 0                # 모음, 자음 개수 세줄 변수
    for c in tmp:                           # 글자가 모음인지 자음인지 정한다
        if c in aeiou:                      
            aeiou_cnt += 1
        else:
            else_cnt += 1
    if aeiou_cnt > 0 and else_cnt > 1:      # 모음과 자음의 조건을 맞추면 저장한다.
        ans.append(''.join(tmp))
ans.sort()                                  # 알파벳 순으로 정렬
for answer in ans:
    print(answer)