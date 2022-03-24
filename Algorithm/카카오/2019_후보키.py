from itertools import combinations

def solution(relation):
    N = len(relation[0])
    key_idx = list(range(N))
    candidate_keys = []
    
    for i in range(1,N+1):
        for candidate in combinations(key_idx, i):  # 모든 조합에 대해
            tmp = []
            for r in relation:
                current_key = []
                for c in candidate:
                    current_key.append(r[c])
                 
                if current_key in tmp:          # 하나라도 중복되는 경우: 식별 불가능
                    break
                else:                           # 하나도 중복 안 된 경우: 식별 가능
                    tmp.append(current_key)
            
            else:
                for ck in candidate_keys:       # 최소성 확인 (구글 검색으로 issubset 사용) 
                    if set(ck).issubset(set(candidate)):
                        break
                else:
                    candidate_keys.append(candidate)
    
    return len(candidate_keys)