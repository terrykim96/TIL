def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    
    for problem in problems:
        max_alp = max(max_alp, problem[0])
        max_cop = max(max_cop, problem[1])

    alp_nec = min(alp, max_alp)
    cop_nec = min(cop, max_cop)
    INF = 10e7
    
    dp = [[INF]*(max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp_nec][cop_nec] = 0
    
    for i in range(alp_nec, max_alp + 1):
        for j in range(cop_nec, max_cop + 1):
            if i + 1 <= max_alp:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)

            for problem in problems:
                if i >= problem[0] and j >= problem[1]:
                    next_alp, next_cop = min(max_alp, i + problem[2]), min(max_cop,j + problem[3])
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop], dp[i][j] + problem[4])
    return dp[-1][-1] 