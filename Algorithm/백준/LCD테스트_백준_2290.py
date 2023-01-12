s, nums = input().split()

# 각 숫자마다 불 들어오는 위치를 리스트로 만들어준다.
info = {'0' : [1, 2, 3, 4, 5, 6],
        '1' : [3, 6], 
        '2' : [2, 3, 4, 5, 7], 
        '3' : [2, 3, 5, 6, 7], 
        '4' : [1, 3, 6, 7], 
        '5' : [1, 2, 5, 6, 7], 
        '6' : [1, 2, 4, 5, 6, 7], 
        '7' : [2, 3, 6], 
        '8' : [1, 2, 3, 4, 5, 6, 7], 
        '9' : [1, 2, 3, 5, 6, 7]
        }

s = int(s)
answer = [[[' 'for i in range(s + 2)]for j in range(2 * s + 3)] for k in range(len(nums))]

def lines(board, idx):      # 각 위치에 맞게 불이 들어오게 설정해준다.
    for i in idx:
        if i == 1:
            for j in range(1, s + 1):
                board[j][0] = '|'
        elif i == 2:
            for j in range(s):
                board[0][j+1] = '-'
        elif i == 3:
            for j in range(1, s+1):
                board[j][s+1] = '|'
        elif i == 4:
            for j in range(s+1, 2*s+1):
                board[j+1][0] = '|'
        elif i == 5:
            for j in range(s):
                board[2*s+2][j+1] = '-'
        elif i == 6:
            for j in range(s+2, 2*s+2):
                board[j][s+1] = '|'
        elif i == 7:
            for j in range(s):
                board[s+1][j+1] = '-'


for i, num in enumerate(nums):
    lines(answer[i], info[num])    

for i in range(2 * s + 3):
    for j in range(len(nums)):
        if j == len(nums) - 1:
            print(''.join(answer[j][i]))

        else:
            print(''.join(answer[j][i]), end = ' ')