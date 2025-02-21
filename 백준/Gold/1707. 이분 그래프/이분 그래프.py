import sys
from collections import defaultdict
from collections import deque

input = sys.stdin.readline

K = int(input())
answer = ""

def bfs(start):
    global isBipartite, visited
    setHash = {"A": [], "B": []}
    deq = deque([["A", start]])
    visited[start] = True
    while deq:
        setName, now = deq.popleft()
        for neighbor in adjList[now]:
                if setName == "A":
                    if neighbor not in setHash["A"]:
                        if not visited[neighbor]:
                            setHash["B"].append(neighbor)
                            visited[neighbor] = True
                            deq.append(["B", neighbor])
                    else:
                        isBipartite = False
                
                if setName == "B":
                    if neighbor not in setHash["B"]:
                        if not visited[neighbor]:
                            setHash["A"].append(neighbor)
                            visited[neighbor] = True
                            deq.append(["A", neighbor])
                    else:
                        isBipartite = False

                if not isBipartite:
                    return

for k in range(K):
    isBipartite = True
    V, E = map(int, input().split())
    
    adjList = defaultdict(list)
    for _ in range(E):
        u, v = map(int, input().split())
        adjList[u].append(v)
        adjList[v].append(u)
    
    visited = [False for _ in range(V + 1)]
    for i in range(1, V + 1):
        if not visited[i]:
            bfs(i)
        if not isBipartite:
            break

    if(isBipartite):
        answer += "YES\n"
    else:
        answer += "NO\n"

print(answer)