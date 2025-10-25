def solution(picks, minerals):
    answer = 0
    
    minerals = minerals[:min(len(minerals), sum(picks) * 5)]
    mineral_cnts = []
    for i in range(0, len(minerals), 5):
        temp = [0, 0, 0]
        for j in range(5):
            mineral_idx = i + j
            if mineral_idx < len(minerals):
                if minerals[mineral_idx] == "diamond":
                    temp[0] += 1
                elif minerals[mineral_idx] == "iron":
                    temp[1] += 1
                elif minerals[mineral_idx] == "stone":
                    temp[2] += 1
        mineral_cnts.append(temp)
    
    mineral_cnts.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
    
    fatigue = 0
    for mineral_cnt in mineral_cnts:
        if picks[0] > 0:
            fatigue += mineral_cnt[0] * 1 + mineral_cnt[1] * 1 + mineral_cnt[2] * 1
            picks[0] -= 1
        elif picks[1] > 0:
            fatigue += mineral_cnt[0] * 5 + mineral_cnt[1] * 1 + mineral_cnt[2] * 1
            picks[1] -= 1
        elif picks[2] > 0:
            fatigue += mineral_cnt[0] * 25 + mineral_cnt[1] * 5 + mineral_cnt[2] * 1
            picks[2] -= 1
        
    answer = fatigue
    return answer