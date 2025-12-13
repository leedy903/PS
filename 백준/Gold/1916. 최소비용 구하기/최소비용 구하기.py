from heapq import heappop, heappush
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = defaultdict(list)

for i in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

departure, arrival = map(int, input().split())

def dijkstra(start, end):
    dist = [float('inf') for _ in range(N + 1)]
    dist[start] = 0
    heap = [(0, start)]

    while heap:
        cost, cur = heappop(heap)
        
        if dist[cur] < cost:
            continue

        for neighbor, weight in graph[cur]:
            if cost + weight < dist[neighbor]:
                dist[neighbor] = cost + weight
                heappush(heap, (dist[neighbor], neighbor))
    
    return dist[end]

print(dijkstra(departure, arrival))