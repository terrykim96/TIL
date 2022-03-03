from collections import Counter

def make_set(string):       # 다중 집합 만드는 함수
    ans = []
    for i in range(len(string) - 1):
        tmp = ''
        for j in range(2):
            tmp += string[i + j]  # 2개씩 묶기
        if tmp.isalpha():
            ans.append(tmp.upper())    # 대문자로 넣기
    return ans

def solution(str1, str2):
    ans = 0

    set1 = make_set(str1)
    set2 = make_set(str2)

    if not set1 and not set2:   # 공집합일 경우
        return 65536

    counter1 = Counter(set1)
    counter2 = Counter(set2)

    print(counter1, counter2)

    union = sum((counter1 | counter2).values())     # 합집합
    inter = sum((counter1 & counter2).values())     # 교집합

    ans = int(inter / union * 65536)
    
    return ans