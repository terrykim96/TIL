T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']    # 성적을 저장한 리스트를 생성한다.

def score(mid, fin, hw):        # 세 점수를 입력 받아 최종 점수를 반환하는 score 함수를 작성한다.
    return mid * 0.35 + fin * 0.45 + hw * 0.2

for i in range(1, T+1):         # 테스트 케이스에 대해
    num, target = map(int, input().split()) # 전체 학생 수와 타겟 학생 수를 입력 받아 저장한다.
    student_dict_tmp = {}
    
    for j in range(1, num + 1): # 모든 학생에 대해 학생을 key로 score 함수로 계산한 최종 점수를 value로 갖는 딕셔너리를 생성한다.
        midterm, final, homework = map(int, input().split())
        scores = score(midterm, final, homework)
        student_dict_tmp.update({str(j): scores})
    # 딕셔너리를 value로 정렬하여 key값을 student_sort라는 리스트에 저장한다.
    student_sort = sorted(student_dict_tmp, key = lambda x: student_dict_tmp[x], reverse= True)

    where = student_sort.index(str(target)) # where이라는 변수에 타겟 학생이 몇등인지 저장한다.
    what_grade = int(where // (num/10))     # what_grade에 학생이 받을 수 있는 성적(등수를 (전체 학생을 10으로 나눈 수)로 나눈 몫)을 저장한다.
    
    print(f'#{i} {grade[what_grade]}')