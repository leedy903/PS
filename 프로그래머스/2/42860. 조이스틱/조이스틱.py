from itertools import permutations

def solution(name):
    answer = 0
    
    INF = int(1e9)
    
    remain = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]
    
    if sum(remain) == 0:
        return answer
    
    vertical_cost = sum(remain)
    
    horizontal_cost = INF
    
    min_visit = []
    for i in range(1, len(remain)):
        if name[i] != 'A':
            min_visit.append(i)
    
    cases = permutations(min_visit, len(min_visit))
    
    for case in cases:
        now = 0
        move_cost = 0
        for _next in case:
            dist = abs(now - _next)
            move_cost += min(dist, len(name) - dist)
            now = _next
    
        horizontal_cost = min(horizontal_cost, move_cost)
        
    
    answer = vertical_cost + horizontal_cost
    return answer