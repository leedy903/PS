def solution(k, tangerine):
    answer = 0
    tangerine_count = dict()
    for t in tangerine:
        if t in tangerine_count:
            tangerine_count[t] += 1
        else:
            tangerine_count[t] = 1
    
    tangerine_count = sorted(tangerine_count.items(), key = lambda x : x[1], reverse = True)
    
    total_count = 0
    for _, count in tangerine_count:
        answer += 1
        total_count += count
        if total_count >= k:
            break
    
    return answer