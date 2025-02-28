import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input())
times = [list(map(int, input().split())) for _ in range(n)]
times.sort()

finish_times = [times[0][1]]

for i in range(1, n):
    if times[i][0] >= finish_times[0]:
        heappop(finish_times)
    heappush(finish_times, times[i][1])
    
print(len(finish_times))