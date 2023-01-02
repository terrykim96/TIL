N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]

cnt = [0] * N           # 학생별 친구 수를 구할 리스트를 만들어준다.

for i in range(N):
    visited = [0] * N   # 친구 여부를 판단하는 visited 리스트를 만들어준다.

    for grade in range(5):  # 6학년까지
        for student in range(N):    # 친구이면 visited 리스트의 원소를 1로 바꿔준다.
            if student != i and students[student][grade] == students[i][grade]:
                visited[student] = 1
        
    cnt[i] = visited.count(1)       # 친구의 수를 세어준다.

print(cnt.index(max(cnt)) + 1)      # 친구가 가장 많은 학생을 찾아준다(index라 1 추가한다.)