import sys
from collections import deque

N = int(sys.stdin.readline())
matrix = [None for _ in range(N)]
for i in range(N):
    matrix[i] = list(map(int, sys.stdin.readline().split()))

dy = [0, -1, 0, 1]
dx = [-1, 0, 1, 0]

baby_shark_weight = 2
baby_shark_exp = 2
by, bx = 0, 0

total_move = 0

def getPreyFishes(by, bx, shark_weight):
    visit = [[False for _ in range (N)] for _ in range(N)]
    time_table = [[0 for _ in range(N)] for _ in range(N)]
    prey_fishes = []

    deq = deque([[by, bx]])
    visit[by][bx] = True
    while deq:
        y, x = deq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < N:
                if not visit[ny][nx] and shark_weight >= matrix[ny][nx]:
                    time_table[ny][nx] = time_table[y][x] + 1
                    visit[ny][nx] = True
                    deq.append([ny, nx])
                    if shark_weight > matrix[ny][nx] and matrix[ny][nx] != 0:
                        prey_fishes.append([time_table[ny][nx], ny, nx])
        
    return sorted(prey_fishes, key=lambda x : (x[0], x[1], x[2]))
    
for i in range(N):
    for j in range(N):
        if matrix[i][j] == 9:
            by, bx = i, j

while True:

    prey_fishes = getPreyFishes(by, bx, baby_shark_weight)

    if len(prey_fishes) == 0:
        break

    move, py, px = prey_fishes[0]

    total_move += move
    matrix[by][bx] = 0
    matrix[py][px] = 0
    by, bx = py, px

    baby_shark_exp -= 1
    if baby_shark_exp == 0:
        baby_shark_weight += 1
        baby_shark_exp = baby_shark_weight
    
print(total_move)

