import sys
input = sys.stdin.readline

v, e = map(int, input().rstrip().split())
edges = [list(map(int, input().rstrip().split())) for _ in range(e)]
dist = [[float('inf') for _ in range(v + 1)] for _ in range(v + 1)]

for edge in edges:
    a, b, c = edge
    dist[a][b] = c

answer = float('inf')
for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    answer = min(answer, dist[k][k])

answer = answer if answer != float('inf') else -1

print(answer)