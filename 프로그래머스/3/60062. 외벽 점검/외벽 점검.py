def solution(n, weak, dist):
    answer = float("inf")
    
    dist.sort(reverse = True)
    
    total_repairs = [()]
    
    for count in range(len(dist)):
        d = dist[count]
        repairs = []
        for i in range(len(weak)):
            j = i
            repair = set()
            while (weak[j] - weak[i]) % n <= d:
                repair.add(weak[j])
                j = (j + 1) % len(weak)
                
                if i == j:
                    answer = min(answer, count + 1)
                    break
            repairs.append(repair)
        
        next_total_repairs = set()
        for repair in repairs:
            for total_repair in total_repairs:
                next_total_repair = repair | set(total_repair)
                if len(next_total_repair) == len(weak):
                    return count + 1
                next_total_repairs.add(tuple(next_total_repair))
        total_repairs = next_total_repairs
        
    return -1