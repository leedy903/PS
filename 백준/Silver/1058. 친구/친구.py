import sys
input = sys.stdin.readline

N = int(input())
friends = [list(input().strip()) for _ in range(N)]

dist = [[float('inf')] * N for _ in range(N)]

for i in range(N):
    for j in  range(N):
        if friends[i][j] == 'Y':
            dist[i][j] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
answer = 0
for i in range(N):
    cnt = 0
    for j in range(N):
        if i != j and dist[i][j] <= 2:
            cnt += 1
    answer = max(answer, cnt)

print(answer)
