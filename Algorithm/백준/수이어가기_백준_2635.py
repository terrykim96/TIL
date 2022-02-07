num = int(input()) 
max_list = []           # 정답을 저장할 리스트와 전체 리스트 길이 지정
list_len = 0

for i in range(num // 2, num + 1):  #  첫 숫자는 주어진 숫자의 절반보다 커야함
    num_list = [num, i]      
    j = 0                           # 인덱스에 사용할 j 지정
    while True:
        new = num_list[j] - num_list[j + 1] # 문제 조건에 맞게 new 지정
        j += 1                      # 인덱스 하나씩 늘리기
        if new < 0:                 # new가 0보다 클 때만 리스트에 append
            break
        num_list.append(new)
        
        if list_len < len(num_list):    # 리스트 길이가 전 for문의 list 길이보다 크면 덮어쓰기
            list_len = len(num_list)
            max_list = num_list[:]

print(list_len)
print(*max_list)    # *로 리스트 요소들 출력
