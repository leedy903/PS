import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
costs = list(map(int, input().split()))
graph = defaultdict(list)
for i in range(N):
    row = list(input().strip())
    for j in range(len(row)):
        if row[j] == '1':
            graph[i].append(j)

parents = [-1 for _ in range(N)]
stack = []
on_stack = [False for _ in range(N)]
id = 0
total_cost = 0

def dfs(cur):
    global id, total_cost
    id += 1
    parents[cur] = id
    stack.append(cur)
    on_stack[cur] = True
    
    parent = parents[cur]
    for next in graph[cur]:
        if parents[next] == -1:
            parent = min(parent, dfs(next))
        elif on_stack[next]:
            parent = min(parent, parents[next])
            
    if parent == parents[cur]:
        scc = []
        while True:
            node = stack.pop()
            on_stack[node] = False
            scc.append(node)
            if cur == node:
                break
        min_cost = float('inf')
        for node in scc:
            min_cost = min(min_cost, costs[node])
        total_cost += min_cost
    return parent

for i in range(N):
    if parents[i] == -1:
        dfs(i)

print(total_cost)