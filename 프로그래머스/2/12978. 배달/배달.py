from heapq import heappush, heappop
def solution(N, road, K):
    answer = 0
    
    INF = float("inf")
    distance = [INF for _ in range(N)]
    
    start = 0
    dijkstra(distance, road, start)

    answer = sum([1 if d <= K else 0 for d in distance])

    return answer

def dijkstra(distance, road, start):
    N = len(distance)
    visit = [False] * N
    visit[start] = True
    distance[start] = 0
    
    for (departure, arrival, cost) in road:
        if departure - 1 == start or arrival - 1 == start:
            distance[start] = min(distance[start], cost)

    while not all(visit):
        nearest_node = get_nearest_node(distance, visit)
        visit[nearest_node] = True
        for (departure, arrival, cost) in road:
            if departure - 1 == nearest_node:
                new_dist = distance[nearest_node] + cost
                if new_dist < distance[arrival - 1]:
                    distance[arrival - 1] = new_dist
            elif arrival - 1 == nearest_node:
                new_dist = distance[nearest_node] + cost
                if new_dist < distance[departure - 1]:
                    distance[departure - 1] = new_dist
                
        
        
def get_nearest_node(distance, visit):
    min_dist = float("inf")
    node_idx = 0
    for i in range(1, len(distance)):
        if distance[i] < min_dist and not visit[i]:
            min_dist = distance[i]
            node_idx = i
    return node_idx