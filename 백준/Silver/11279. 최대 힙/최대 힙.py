import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
heap = []
commands = [int(input()) for _ in range(n)]

for command in commands:
    if command == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heappop(heap))
    else:
        heappush(heap, -command)