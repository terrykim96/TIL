def merge_sort(arr):
    global cnt  # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우 cnt += 1
    # 원소가 1개이면 그냥 그대로 return
    #   이유 : 이미 정렬된 배열임
    if len(arr) == 1:
        return arr

    # 배열의 원소가 2개 이상이면 배열을 두개로 나눠서 각각 정렬된 배열을 return 받는다.
    mid = len(arr) // 2
    left_list = merge_sort(arr[:mid])
    right_list = merge_sort(arr[mid:])

    l_len = len(left_list)
    r_len = len(right_list)

    # now : 원본 배열의 index
    # left : 왼쪽 배열의 index
    # right : 오른쪽 배열의 index
    now = left = right = 0

    # 정렬된 왼쪽 배열과 오른쪽 배열을
    # 첫번째 index부터 마지막 index까지 비교하면서 작은 값 부터 가져온다.
    # 두 배열 중 하나라도 탐색이 끝나면 반복문 종료
    while left < l_len and right < r_len:
        if left_list[left] <= right_list[right]:
            arr[now] = left_list[left]
            left += 1
        else:
            arr[now] = right_list[right]
            right += 1
        now += 1

    # 왼쪽 배열의 탐색이 끝났다면 (즉, 오른쪽 배열에 값이 남아있으면)
    if left == l_len:
        # 가져오지 않은 값들을 다 가져온다.
        for i in range(right, r_len):
            arr[now] = right_list[i]
            now += 1
    # 오른쪽 배열의 탐색이 끝났다면 (즉, 왼쪽 배열에 값이 남아있으면)
    elif right == r_len:
        # 왼쪽 배열의 마지막 원소가 오른쪽 배열의 마지막 원소보다 크기때문에
        # 왼쪽 배열에 값이 남아있는 것이다. -> 카운팅
        cnt += 1
        # 가져오지 않은 값들을 다 가져온다.
        for i in range(left, l_len):
            arr[now] = left_list[i]
            now += 1

    # 병합 정렬된 배열을 리턴
    # 마지막 return인 경우 : 최종적으로 병합 정렬된 배열을 리턴
    # 그렇지 않은 경우 : left or right 변수로 병합 정렬된 중간 결과물을 리턴
    return arr

    
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = list(map(int, input().split()))

    cnt = 0
    merge_sort(numbers)

    print(f'#{test_case} {numbers[N//2]} {cnt}')