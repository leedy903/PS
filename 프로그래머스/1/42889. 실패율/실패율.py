def solution(N, stages):
    stages.sort()
    now_in_stage = [stages.count(s + 1) for s in range(N + 1)]
    stage_challenger = [sum(now_in_stage[i:]) for i in range(N)]
    
    failures = {i + 1 : 0 for i in range(N)}
    
    for i in range(N):
        if stage_challenger[i] != 0:
            failures[i + 1] = now_in_stage[i]/stage_challenger[i]
            
    
    return sorted(failures, key = lambda x : failures[x], reverse = True)
    