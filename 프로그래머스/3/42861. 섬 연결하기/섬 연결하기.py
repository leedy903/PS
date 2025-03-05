from heapq import heappush, heappop

parents = []
def solution(n, costs):
    global parents
    answer = 0
    parents = [i for i in range(n)]
    
    pq = []
    for cost in costs:
        u, v, w = cost
        heappush(pq, [w, u, v])
    
    edgeCount = 0
    
    while pq:
        w, u, v = heappop(pq)
        
        u = find(u)
        v = find(v)
        if u != v:
            answer += w
            edgeCount += 1
            union(u, v)
    
        if edgeCount == n - 1:
            break
    
    return answer


def find(x):
    global parents
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(a, b):
    global parents
    a = find(a)
    b = find(b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b