import sys
from collections import defaultdict
from heapq import heappush, heappop

input = sys.stdin.readline

n, m, x = map(int, input().strip().split())
edges = defaultdict(list)

for _ in range(m):
    a, b, w = map(int, input().strip().split())
    edges[a].append([b, w])

def dijkstra(start):
    dist = [float('inf') for _ in range(n + 1)]
    dist[start] = 0
    pq = [(start, 0)]
    while pq:
        cur_node, cost = heappop(pq)

        if (dist[cur_node] < cost):
            continue

        for edge in edges[cur_node]:
            next_node, next_cost = edge
            new_cost = dist[cur_node] + next_cost
            if dist[next_node] > new_cost:
                dist[next_node] = new_cost
                heappush(pq, (next_node, new_cost))

    return dist

round_trip_dist = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    one_way_dist = dijkstra(i)
    
    if i == x:
        for j in range(1, n + 1):
            round_trip_dist[j] += one_way_dist[j]
    else:
        round_trip_dist[i] += one_way_dist[x]

print(max(round_trip_dist))