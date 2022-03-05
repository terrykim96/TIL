def solution(cacheSize, cities):
    ans = 0
    cache = []
    if cacheSize == 0:
        return len(cities) * 5 

    for city in cities: 
        if city.lower() in cache:       # cache hit
            cache.remove(city.lower())
            cache.append(city.lower())  # 해당 도시를 리스트의 맨 뒤로 보내기
            ans += 1
        
        else:                           # cache miss
            if len(cache) == cacheSize:
                cache.pop(0)            # LRU 알고리즘으로 캐시 교체
            cache.append(city.lower())
            ans += 5
    
    return ans