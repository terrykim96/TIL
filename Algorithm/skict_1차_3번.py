'''
가로 1칸, 세로 1칸의 크기를 갖는 정사각형으로 이루어진 가로 width칸, 세로 height칸의 격자가 있습니다. 일부 정사각형에는 "왼쪽 위의 점과 오른쪽 아래점을 잇는" 대각선이 있습니다. 이 격자에서 다음 조건을 만족하는 경로의 개수를 구하고자 합니다.

좌측 하단의 끝점에서 우측 상단의 끝점으로 가는 경로입니다.
대각선을 정확히 1번 이용해야 합니다.
1, 2번 조건을 만족하는 전제 하에서 최단거리 경로여야 합니다.
예를 들어, 다음 그림은 한 격자가 주어졌을 때, 해당 격자에서 1~3번 조건을 만족하는 경로를 모두 나타낸 것입니다.

격자의 가로 길이 width, 세로 길이 height, 대각선이 위치한 정사각형의 정보 diagonals가 매개변수로 주어집니다. 주어진 조건을 모두 만족하는 경로의 개수를 10,000,019로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ width ≤ 250
1 ≤ height ≤ 250
1 ≤ diagonals의 길이 ≤ width x height
diagonals의 각 행은 두 정수 [x, y]로 이루어져 있으며, 왼쪽에서부터 x번째, 아래에서부터 y번째 사각형에 대각선이 있음을 의미합니다.
1 ≤ x ≤ width
1 ≤ y ≤ height
똑같은 (x, y) 순서쌍은 2번 이상 등장하지 않습니다.

입출력 예
width	height	diagonals	result
2	2	[[1,1],[2,2]]	12
51	37	[[17,19]]	3225685

'''

import math

def count(w, h):
    ans = math.factorial(w + h) // (math.factorial(w) * math.factorial(h))
    return ans

def solution(width, height, diagonals):
    answer = 0

    for dig in diagonals:
        answer += count(dig[0], dig[1] - 1) * count(width - dig[0] + 1, height - (dig[1] - 1) - 1)
        answer += count(dig[0] - 1, dig[1]) * count(width - (dig[0] - 1) - 1, height - dig[1] + 1)

    answer = answer % 10000019
    return answer