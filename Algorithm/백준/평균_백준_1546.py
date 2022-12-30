N = int(input())
scores = list(map(int, input().split()))
max_score = max(scores)     # 과목 점수들 중 최댓값을 저장한다.

for i in range(N):
    scores[i] = (scores[i] / max_score) * 100     # 문제에서 제시한 식에 따른 점수를 계산해서 score 요소를 바꿔준다.

print(sum(scores)/N)        # 새로운 점수들의 평균을 구해준다.