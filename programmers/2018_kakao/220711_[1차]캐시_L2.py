from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for city in cities:
        if city.upper() not in cache:
            if cache and len(cache) >= cacheSize:
                cache.popleft()
            if cacheSize > 0:
                cache.append(city.upper())
            answer += 5
        else:
            answer += 1
            idx = list(cache).index(city.upper())
            del cache[idx]
            cache.append(city.upper())
    return answer