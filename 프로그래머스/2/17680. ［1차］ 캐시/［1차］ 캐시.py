from collections import deque
def solution(cacheSize, cities):
    
    cache = deque(maxlen = cacheSize)
    execTime = 0
    
    for city in cities:
        city = city.lower()
        
        if city in cache:
            cache.remove(city)
            execTime += 1
        else:
            execTime += 5
            
        cache.append(city)
            
    answer = execTime
        
    return answer