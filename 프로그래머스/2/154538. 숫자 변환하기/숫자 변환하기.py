from heapq import heappush, heappop
def solution(x, y, n):
    answer = 0
    costs = [float('inf') for _ in range(y + 1)]
    costs[x] = 0
    heap = [[0, x]]
    while heap:
        cur_cost, cur_num = heappop(heap)
        next_num = cur_num + n
            
        for next_num in (cur_num + n, cur_num * 2, cur_num * 3):
            if next_num <= y and costs[next_num] > cur_cost + 1:
                costs[next_num] = cur_cost + 1
                heappush(heap, [cur_cost + 1, next_num])

    answer = costs[y]

    if answer == float('inf'):
        answer = -1
    
    return answer