from collections import deque
def solution(stones, k):
    max_stones = [stones[0]]
    deq = deque([[stones[0], 0]])
    for i in range(1, len(stones)):
        stone = stones[i]
        while len(deq) > 0 and deq[-1][0] < stone:
            deq.pop()
            
        deq.append([stone, i])
        
        while i - deq[0][1] >= k:
            deq.popleft()
        
        max_stones.append(deq[0][0])
    answer = min(max_stones[k - 1:])
    return answer