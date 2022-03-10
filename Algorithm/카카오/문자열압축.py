def solution(s):
    answer = 10000

    for n in range(1, len(s)//2 + 2):   # 단위 문자열의 최대 길이는 (총 문자열 길이)//2이다. (길이가 1개일 경우를 위해 +2)
        string = ''         # 압축이 끝난 뒤 최종 문자열
        cnt = 1
        tmp = s[: n]        # 첫 단위 문자열을 설정한다.

        for i in range(n, len(s) + n, n):   # 단위 문자열의 길이만큼씩 문자를 비교한다.
            if tmp == s[i : i + n]: # 단위 문자열이 겹치면 cnt에 1을 추가한다.
                cnt += 1
            else:           # 겹치지 않으면
                if cnt:     # cnt가 1일때는 cnt 없이 문자열을 추가한다. (1ab가 아니라 ab)
                    string += tmp
                else:       # cnt가 1이 아니면 cnt와 문자열을 추가한다. (2ab)
                    string += str(cnt) + tmp
                tmp = s[i : i + n]  # tmp와 cnt를 초기화해준다.
                cnt = 1

        answer = min(answer, len(string))   # 지금까지의 최소 answer 값을 저장해준다.
    return answer
