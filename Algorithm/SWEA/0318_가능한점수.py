T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))
    possible = [1] + [0] * sum(scores)

    for score in scores:
        for i in range(len(possible) - score, -1, -1):
            if possible[i]:
                possible[i + score] = 1
                
    print(f'#{test_case} {sum(possible)}')