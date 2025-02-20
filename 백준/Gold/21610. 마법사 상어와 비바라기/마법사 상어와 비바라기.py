import sys
N, M = map(int, sys.stdin.readline().split())
baskets = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
commands = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for d, s in commands:
    for i, cloud in enumerate(clouds):        
        cy, cx = cloud
        clouds[i] = [(cy + dy[d - 1] * s) % N, (cx + dx[d - 1] * s) % N]

    rained = [[False] * N for _ in range(N)]
    for cy, cx in clouds:
        baskets[cy][cx] += 1
        rained[cy][cx] = True
        
    for cy, cx in clouds:
        has_water = 0
        for i in range(1, 8, 2):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if baskets[ny][nx] > 0:
                    has_water += 1
        baskets[cy][cx] += has_water

    new_clouds = []
    for i in range(N):
        for j in range(N):
            if baskets[i][j] > 1 and not rained[i][j]:
                new_clouds.append([i, j])
                baskets[i][j] -= 2

    clouds = new_clouds

water = 0
for i in range(N):
    for j in range(N):
        water += baskets[i][j]
print(water)