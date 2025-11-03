import sys
from collections import deque
input = sys.stdin.readline

def char_to_idx(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A')
    return ord(c) - ord('a') + 26

MAX_V = 52
capacity = [[0 for _ in range(MAX_V)] for _ in range(MAX_V)]
graph = [[0 for _ in range(MAX_V)] for _ in range(MAX_V)]

N = int(input())
for _ in range(N):
    u_char, v_char, w = input().split()
    u, v = char_to_idx(u_char), char_to_idx(v_char)
    w = int(w)

    capacity[u][v] += w
    capacity[v][u] += w

    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)

def bfs(source, sink, parent):
    visited = [False for _ in range(MAX_V)]
    deq = deque()
    deq.append(source)
    visited[source] = True
    while deq:
        cur_node = deq.popleft()
        for next_node in graph[cur_node]:
            if not visited[next_node] and capacity[cur_node][next_node] > 0:
                visited[next_node] = True
                parent[next_node] = cur_node
                if next_node == sink:
                    return True
                deq.append(next_node)
    return False

def edmonds_karp(source, sink):
    total = 0
    parent = [-1 for _ in range(MAX_V)]

    while bfs(source, sink, parent):
        path_flow = float('inf')
        cur_node = sink
        while cur_node != source:
            next_node = parent[cur_node]
            path_flow = min(path_flow, capacity[next_node][cur_node])
            cur_node = next_node
        
        cur_node = sink
        while cur_node != source:
            next_node = parent[cur_node]
            capacity[cur_node][next_node] += path_flow
            capacity[next_node][cur_node] -= path_flow
            cur_node = next_node
        
        total += path_flow
    return total

source = char_to_idx('A')
sink = char_to_idx('Z')
print(edmonds_karp(source, sink))