from collections import deque

def solution(n, roads, sources, destination):    
    
    answer = []
    edges = {i : [] for i in range(1, n + 1)}
    
    for u, v in roads:
        edges[u].append(v)
        edges[v].append(u)
    
    deq = deque([])
    
    visited = [False for _ in range(n + 1)]
    visited[destination] = True

    distance = [float("inf") for _ in range(n + 1)]
    distance[destination] = 0

    deq.append(destination)
        
    while deq:
        now = deq.popleft()
        for node in edges[now]:
            if not visited[node]:
                distance[node] = distance[now] + 1
                visited[node] = True
                deq.append(node)

    for source in sources:
        arrival_time = distance[source] if distance[source] != float("inf") else -1
        answer.append(arrival_time)
    
    return answer