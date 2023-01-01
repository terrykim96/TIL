switch_len = int(input())
switch_list = list(map(int, input().split()))
student_info = []
student_num = int(input()) # 테스트 케이스의 개수

for _ in range(student_num):
    student_info.append(list(map(int, input().split())))

def boys(num):              # 남자
    for i in range(switch_len):
        if (i+1) % num == 0:
            switch_list[i] = int(not switch_list[i])
            
def girls(num):             # 여자
    if num == 1 or num == switch_len:
        switch_list[num-1] =  int(not switch_list[num-1])
    else:
        for i in range(int(switch_len/2)):
            if (num - 1 - i) >= 0 and (num - 1 + i) <= (switch_len - 1):
                if switch_list[num - 1 - i] == switch_list[num - 1 + i]:
                    switch_list[num - 1 + i], switch_list[num - 1 - i] = int(not switch_list[num - 1 + i]),  int(not switch_list[num - 1 - i])
                else:
                    break


for i in range(student_num):
    if student_info[i][0] == 1:
        boys(student_info[i][1])
    else:
        girls(student_info[i][1])


for i in range(switch_len):
    if i in [19, 39, 59, 79]:
        print(switch_list[i])
    else:
        print(switch_list[i], end= ' ')