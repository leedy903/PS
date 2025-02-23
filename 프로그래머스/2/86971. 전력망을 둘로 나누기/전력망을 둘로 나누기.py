def solution(n, wires):
    answer = float('inf')
    for i in range(len(wires)):
        roots = {}
        parent = list(range(n + 1))
        for j in range(len(wires)):
            if i == j:
                continue
            v1, v2 = wires[j]
            union_parent(parent, v1, v2)
        
        for j in range(1, n + 1):
            root = find_parent(parent, parent[j])
            if root in roots:
                roots[root] += 1
            else:
                roots[root] = 1
    
        c1, c2 = roots.values()
        answer = min(answer, abs(c1 - c2))    
    return answer

def find_parent(parent, wire):
    if parent[wire] != wire:
        parent[wire] = find_parent(parent, parent[wire])
    return parent[wire]


def union_parent(parent, wire1, wire2):
    parent1 = find_parent(parent, wire1)
    parent2 = find_parent(parent, wire2)
    
    if parent1 < parent2:
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2