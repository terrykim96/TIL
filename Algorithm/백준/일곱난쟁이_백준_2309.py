smaller = list(int(input()) for _ in range(9))  # smaller 리스트에 난쟁이들 키를 저장한다.

height = sum(smaller)           # 난쟁이 키들의 총합을 저장한다.

for i in range(9):              # 난쟁이들 중 2명을 제외하고 키의 합이 100이 되면 난쟁이들 저장
    for j in range(i + 1, 9):
        if height - (smaller[i] + smaller[j]) == 100:
            not1, not2 = smaller[i], smaller[j]

            smaller.remove(not1)
            smaller.remove(not2)
            smaller.sort()

            for person in smaller:
                print(person)
            break

    if len(smaller) < 9:        # 인덱스 에러를 없애기 위해 remove 후에는 break 
        break