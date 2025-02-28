from copy import deepcopy
from itertools import combinations
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

dx = [-1, 0 ,1, 0]
dy = [0, -1, 0, 1]

# 처음에 주어진 남은 빈칸의 모든 숫자만큼 나오면 return
# 남은 빈칸이 최대값보다 작으면 return

max_safe = 0
wall = 0
virus = 0
empty = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            empty.append([i, j])
        elif lab[i][j] == 1:
            wall += 1
        elif lab[i][j] == 2:
            virus += 1

empty_combinations = list(combinations(empty, 3))

def virus_spread(x, y, newlab):
    virus = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < M and ny < N and newlab[ny][nx] == 0:
            newlab[ny][nx] = 3
            virus += virus_spread(nx, ny, newlab)
    return virus

def safe_count(empty_combi, newlab):
    global max_safe
    for e in range(3):
        newlab[empty_combi[e][0]][empty_combi[e][1]] = 1

    total_virus = virus

    for i in range(N):
        for j in range(M):
            if newlab[i][j] == 2:
                spread_virus = virus_spread(j, i, newlab) - 1
                total_virus += spread_virus
            if N*M - total_virus - wall - 3 <= max_safe:
                return 0

    return N*M - total_virus - wall - 3
    

for empty_combi in empty_combinations:
    newlab = deepcopy(lab)
    max_safe = max(max_safe, safe_count(empty_combi, newlab))

print(max_safe)
