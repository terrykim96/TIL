def solution(n, arr1, arr2):
    ans = []
    
    for i in range(n):      # 전체 수에 대해
        bin_str = bin(arr1[i] | arr2[i])[2:]    # bin 연산과 or 연산을 합쳐서 두 지도를 합쳐준다.
        ans.append(('0' * (n - len(bin_str)) + bin_str).replace('1', '#').replace('0', ' '))    # bin 연산 후에 앞에 0을 채워주고, 1과 0을 #과 공백으로 바꿔준다.
    
    return ans