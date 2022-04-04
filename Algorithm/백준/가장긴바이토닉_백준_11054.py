# 증가하는 부분이 긴 수열 두개를 앞, 뒤에서 부터 하나씩 찾아서 합친다. 그 후 길이가 최대인 수열을 찾는다.

N = int(input())
array = list(map(int, input().split()))
reverse_array = array[::-1]

d_front = [1] * N
d_rear = [1] * N

for i in range(N):
    for j in range(i):
        if array[j] < array[i]: # 앞에서부터
            d_front[i] = max(d_front[i], d_front[j]+1)

        if reverse_array[j] < reverse_array[i]: # 뒤에서부터
            d_rear[i] = max(d_rear[i], d_rear[j]+1)

ans = [0] * N
for i in range(N):
    ans[i] = d_front[i] + d_rear[N - 1 - i] - 1   # 가운데 수가 겹치므로(각 수열의 끝은 같으므로) 더한 길이에서 1을 빼준다.

print(max(ans))