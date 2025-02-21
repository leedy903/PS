import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
dist = [float('inf') for _ in range(100_001)]

answer = float('inf')
dist[n] = 0
deq = deque([n])
while deq:
    cur_pos = deq.popleft()
    
    if cur_pos == k:
        answer = dist[k]
        break

    next_pos = cur_pos * 2
    if next_pos < len(dist) and dist[next_pos] > dist[cur_pos]:
        dist[next_pos] = dist[cur_pos]
        deq.appendleft(next_pos)
    
    for next_pos in (cur_pos - 1, cur_pos + 1):
        if 0 <= next_pos < len(dist) and dist[next_pos] > dist[cur_pos] + 1:
            dist[next_pos] = dist[cur_pos] + 1
            deq.append(next_pos)
        
print(answer)