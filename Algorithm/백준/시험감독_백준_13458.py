N = int(input())
students = list(map(int, input().split()))
b, c = map(int, input().split())

ans = N                     # 최소 감독관 수를 지정한다.(방에 총 감독관 수 한명씩)

for i in range(N):
    if students[i] <= b:    # 총감독관이 볼 수 있는 학생보다 적으면 넘어간다.
        continue
    
    else:
        if (students[i] - b) % c != 0:  # 0으로 나눠떨어지지 않으면 (몫+1)명, 아니면 (몫)명만큼 감독관을 추가해준다.
            ans += ((students[i] - b) // c + 1)
        
        else:
            ans += ((students[i] - b) // c)
            
print(ans)