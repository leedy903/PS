from heapq import heapify, heappop, heappush
def solution(scoville, K):
    count = 0
    
    heapify(scoville)
    while True:
        smallest = heappop(scoville)
        if smallest >= K:
            break
        count += 1
        
        if len(scoville) == 0:
            count = -1
            break
        smaller = heappop(scoville)
        mix = smallest + smaller * 2
        heappush(scoville, mix)
    
        
    return count