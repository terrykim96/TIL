T=int(input())

for _ in range(T):
    N = int(input())
    rank = list(map(int, input().split()))

    team_num = max(rank)
    score = [0] * (team_num + 1)
    team_cnt = [0] * (team_num + 1)
    fifth_team = []

    new_rank = [num for num in rank if rank.count(num) == 6]

    for idx, team in enumerate(new_rank):
        if team_cnt[team] >= 4:
            fifth_team.append(team)
            continue

        score[team] += (len(new_rank) - idx)
        team_cnt[team] += 1

    if score.count(max(score)) != 1:
        ans = fifth_team[0]
    else:
        ans = score.index(max(score))

    print(ans)