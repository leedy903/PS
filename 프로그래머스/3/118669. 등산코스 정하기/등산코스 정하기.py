from heapq import heappush, heappop
from collections import defaultdict
edges = defaultdict(list)

def solution(n, paths, gates, summits):
    global edges
    answer = []
    
    for path in paths:
        u, v, w = path
        edges[u].append([v, w])
        edges[v].append([u, w])
    
    summits = list(set(summits))
    summits.sort()
    
    intensity = bfs(gates, summits, n)
    
    min_intensity = float("inf")
    
    for summit in summits:
        if intensity[summit] < min_intensity:
            min_intensity = intensity[summit]
            answer = [summit, min_intensity]
    
    return answer


def bfs(starts, summits, n):
    global edges

    intensity = [float("inf") for _ in range(n + 1)]
    pq = []

    for start in starts:
        intensity[start] = 0
        heappush(pq, [0, start])
    
    while pq:
        cost, now = heappop(pq)
        
        if binarySearch(summits, now):
            continue
        
        if intensity[now] < cost:
            continue
        
        for neighbor, weight in edges[now]:
            next_cost = max(weight, intensity[now])
            if next_cost < intensity[neighbor]:
                intensity[neighbor] = next_cost
                heappush(pq, [next_cost, neighbor])
            
    return intensity


def binarySearch(summits, target):
    start = 0
    end = len(summits) - 1
    while start <= end:
        mid = (start + end) // 2
        if summits[mid] == target:
            return True
        elif summits[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return False
    
    
    
    
    
    
    
    
    
    