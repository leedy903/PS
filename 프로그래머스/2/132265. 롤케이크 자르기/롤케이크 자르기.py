from collections import defaultdict
def solution(topping):
    answer = 0
    old = defaultdict(int)
    young = defaultdict(int)
    
    for t in topping:
        young[t] += 1
    
    for i in range(len(topping)):
        old[topping[i]] += 1
        young[topping[i]] -= 1
        
        if young[topping[i]] == 0:
            young.pop(topping[i])
        
        if len(old.items()) == len(young.items()):
            answer += 1
    return answer