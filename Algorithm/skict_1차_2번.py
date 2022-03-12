'''
자연수 n과 시계/반시계 방향을 결정하는 boolean 값 clockwise가 주어집니다. 입출력 예 설명의 그림과 같이 소용돌이 모양(clockwise가 참이면 시계방향, 거짓이면 반시계방향)으로 n x n 정수 배열을 채워 return 하도록 solution 함수를 완성해주세요.
'''


def solution(n, clockwise):
    answer = [[0]*n for _ in range(n)]

    num = 1
    first = 0
    last = n -1

    while True:
        answer[first][first] = num
        answer[first][last] = num
        answer[last][first] = num
        answer[last][last] = num

        middle = []
        for i in range(num + 1, (num + 1) + (last - first - 1)):
            middle.append(i)

        if not len(middle):
            break

        for i, j in enumerate(range(first + 1, last)):
            answer[first][j] = middle[i]

        for i, j in enumerate(range(last - 1, first, -1)):
            answer[last][j] = middle[i]

        for i, j in enumerate(range(first + 1, last)):
            answer[j][last] = middle[i]

        for i, j in enumerate(range(last - 1, first, -1)):
            answer[j][first] = middle[i]

        num = middle[-1] + 1
        first += 1
        last -= 1
        
    if clockwise == False:
        answer = [list(x) for x in zip(*answer)]
    return answer