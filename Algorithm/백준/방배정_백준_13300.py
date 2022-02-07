import math

N, K = map(int, input().split())
student = [[0] * 6 for _ in range(3)] #성별 / 학년별 학생 리스트

for _ in range(N):
    gender, grade = map(int, input().split())    # student 리스트에 학생 저장
    student[gender][grade - 1] += 1
        
room = 0

for i in student:
    for j in i:
        room += math.ceil(j / K) # 올림해서 방 수 출력 (몫을 사용하니까 안돼서.. 이유 알려주실분 ㅠ)
print(room)