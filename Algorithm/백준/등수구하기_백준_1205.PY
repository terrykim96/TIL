N, new, P = map(int, input().split())

score = []

if N:
	score = list(map(int, input().split()))
	score.append(new)
	score.sort(reverse=True)
	rank = score.index(new) + 1     # 새로운 점수의 등수를 저장해준다.

	if rank > P:                    # rank가 P보다 크면 -1을 출력한다.
		print(-1)

	else:                           # rank가 P보다 작은 경우
		if N == P and new == score[-1]: # N과 P가 같고 가장 낮은 점수가 새로운 점수라면 -1을 출력한다.
			print(-1)

		else:                           # 아니라면 새로운 점수의 등수를 출력한다.
			print(rank)

else:                               # N이 0이면 1을 출력한다.
	print(1)