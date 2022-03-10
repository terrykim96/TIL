def change(n, q):       # n진수로 바꿔주는 함수
    arr = '0123456789ABCDEF'
    ret = ''

    if q == 0:
        return '0'

    while q > 0:
        ret = arr[q % n] + ret
        q = q // n

    return ret

def solution(n, t, m, p):
    answer = ''
    tmp = ''

    for i in range(0, t * m):   # t*m 까지의 숫자를 n진수로 바꿔준다.
        tmp += change(n, i)

    for i in range(p - 1, m * t, m):
        answer += tmp[i]    # 튜브가 말해야 하는 숫자를 찾아준다.

    return answer