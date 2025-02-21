def solution(diffs, times, limit):
    answer = 0
    
    diffs = [0] + diffs
    times = [0] + times
    
    min_level, max_level = 1, max(diffs)
    while min_level <= max_level:
        level = (min_level + max_level) // 2
        total_sol_time = 0
        for i in range(1, len(diffs)):
            total_sol_time += max(0, diffs[i] - level) * (times[i] + times[i - 1]) + times[i]
        
        if total_sol_time <= limit:
            max_level = level - 1
        else:
            min_level = level + 1

    return min_level