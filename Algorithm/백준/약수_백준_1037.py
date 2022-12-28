N = int(input())

numbers = list(map(int, input().split()))

numbers.sort()          # 작은 수부터 정렬

ans = (numbers[0] * numbers[-1])    # 제일 작은 수와 제일 큰 수 곱하기

print(ans)