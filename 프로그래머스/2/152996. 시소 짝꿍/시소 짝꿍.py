from collections import Counter

def solution(weights):
    counter = Counter(weights)
    answer = 0
    
    for weight, count in counter.items():
        answer += count * (count - 1) // 2
        answer += count * counter[weight * 2]
        answer += count * counter[weight * 3 // 2] if weight * 3 % 2 == 0 else 0 
        answer += count * counter[weight * 4 // 3] if weight * 4 % 3 == 0 else 0 
        
    return answer