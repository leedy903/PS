import sys
from collections import deque
input = sys.stdin.readline

dh = [0, 0, 0, 0, -1, 1]
dy = [-1, 0, 1, 0, 0, 0]
dx = [0, -1, 0, 1, 0, 0]

M, N, H = map(int, input().rstrip().split())
tomato_storage = []

for i in range(H):
    tomato_box = []
    for j in range(N):
        tomato_box.append(list(map(int, input().rstrip().split())))
    tomato_storage.append(tomato_box)

deq = deque([])
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato_storage[i][j][k] == 1:
                deq.append([i, j, k])

while deq:
    h, y, x = deq.popleft()
    for d in range(6):
        nh = h + dh[d]
        ny = y + dy[d]
        nx = x + dx[d]

        if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M:
            if tomato_storage[nh][ny][nx] == 0:
                tomato_storage[nh][ny][nx] = tomato_storage[h][y][x] + 1
                deq.append([nh, ny, nx])

def get_day():
    day = 0
    for h in range(H):
        for y in range(N):
            for x in range(M):
                if tomato_storage[h][y][x] == 0:
                    return -1
                day = max(day, tomato_storage[h][y][x])
    return day - 1

day = get_day()
print(day)