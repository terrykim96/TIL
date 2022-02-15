N = int(input())
dice_idx = [5, 3, 4, 1, 2, 0]   # 주사위 반대편 index (0-5, 1-3, 2-4)
dice = []
for _ in range(N):
    dice.append(list(map(int, input().split())))

ans = 0         # 최댓값 저장할 변수 지정

for i in range(6):  # 첫번째 주사위에 대해 6가지 모두 순회
    result = 0      # 각 경우에 대해 주사위마다 옆면의 최댓값을 저장할 리스트
    tmp = [1, 2, 3, 4, 5, 6]    # 주사위 모든 숫자
    tmp.remove(dice[0][i])      # 아랫면과 top에 저장한 윗면 index로 찾은 윗면 숫자 삭제
    top = dice[0][dice_idx[i]]
    tmp.remove(top)
    result += max(tmp)          # 옆면 중 최댓값을 result에 더해준다.

    for j in range(1, N):       # 두번째 주사위부터
        tmp = [1, 2, 3, 4, 5, 6]    # 첫번째 주사위와 같은 과정 반복해준다.
        tmp.remove(top)
        top = dice[j][dice_idx[dice[j].index(top)]]
        tmp.remove(top)
        result += max(tmp)
    
    if ans < result:            # result 중 최댓값 저장
        ans = result

print(ans)