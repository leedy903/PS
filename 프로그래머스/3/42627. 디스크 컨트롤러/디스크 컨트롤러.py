from heapq import heapify, heappush, heappop
def solution(jobs):
    answer, current, i, start = 0, 0, 0, -1
    jobs_heap = []
    
    while i < len(jobs):
        for job in jobs:
            if start < job[0] <= current:
                heappush(jobs_heap, [job[1], job[0]])
        
        if len(jobs_heap) > 0:
            take, request = heappop(jobs_heap)
            start = current
            current += take
            answer += current - request
            i += 1
        else:
            current += 1
    
    return answer // len(jobs)