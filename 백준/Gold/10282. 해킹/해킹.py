import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(start):
    dist = [float('inf') for _ in range(n + 1)]

    dist[start] = 0
    pq = [(start, 0)]
    while pq:
        cur_node, cur_cost = heappop(pq)

        if (dist[cur_node] < cur_cost):
            continue
    
        for next_node, next_cost in graph[cur_node]:
            new_cost = dist[cur_node] + next_cost
            if new_cost < dist[next_node]:
                dist[next_node] = new_cost
                heappush(pq, (next_node, new_cost))
    return dist

T = int(input())
for test_case in range(T):
    n, d, c = map(int, input().split())
    graph = defaultdict(list)
    for i in range(d):
        a, b, s = map(int, input().split())

        graph[b].append([a, s])
    
    infected_times = dijkstra(c)
    count = 0
    min_time = 0
    for time in infected_times:
        if time != float('inf'):
            count += 1
            if min_time < time:
                min_time = time
    print(count, min_time)