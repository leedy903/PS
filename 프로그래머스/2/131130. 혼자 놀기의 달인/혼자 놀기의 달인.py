from collections import Counter
def solution(cards):
    n = max(cards)
    parents = list(range(n + 1))
    group = Counter()
    
    def find(x):
        if x != parents[x]:
            parents[x] = find(parents[x])
        return parents[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b:
            parents[b] = a
        else:
            parents[a] = b
    
    for i in range(len(cards)):
        union(i + 1, cards[i])
        
    for i in range(n + 1):
        group[find(i)] += 1
    
    rank = group.most_common()
    
    answer = rank[0][1] * rank[1][1] if rank[0][1] < n else 0
    return answer