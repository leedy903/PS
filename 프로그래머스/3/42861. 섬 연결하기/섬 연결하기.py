def solution(n, costs):
    answer = 0
    parent = list(range(n))
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    
    costs.sort(key=lambda x : x[2])
    
    cnt = 0
    for a, b, cost in costs:
        a = find(a)
        b = find(b)
        
        if a != b:
            union(a, b)
            answer += cost
            cnt += 1
            
        if n - 1 <= cnt:
            break
        
    return answer
