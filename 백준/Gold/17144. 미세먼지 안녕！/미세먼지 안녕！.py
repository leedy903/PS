import sys
R, C, T = map(int, sys.stdin.readline().split())

room = [[] for _ in range(R)]
air_cleaners = []
for i in range(R):
    room[i] = list(map(int, sys.stdin.readline().split()))
    if -1 in room[i]:
        air_cleaners.append(i)

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def diffuse(dust_room: list) -> list:
    diffusing_room = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            fine_dust = dust_room[i][j]
            if fine_dust > 0:
                diffuse_count = 0
                for k in range(4):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < C and 0 <= ny < R and dust_room[ny][nx] != -1:
                        diffusing_room[ny][nx] += fine_dust//5
                        diffuse_count += 1
                dust_room[i][j] -= (fine_dust//5) * diffuse_count
    for i in range(R):
        for j in range(C):
            dust_room[i][j] += diffusing_room[i][j]
    
    return dust_room


def rotate(dust_room: list, y_direction: int, air_cleaner: int) -> list:
    dx = [1, 0, -1, 0]
    dy = [0, -y_direction, 0, y_direction]
    direction = 0
    before = 0
    y, x = air_cleaner, 1
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if y == air_cleaner and x == 0:
            break
        if 0 > nx or nx >= C or 0 > ny or ny >= R:
            direction += 1
            continue
        temp = dust_room[y][x]
        dust_room[y][x] = before
        before = temp
        
        x = nx
        y = ny
    
    return dust_room


def total_fine_dust(dust_room: list) -> int:
    total_fd = 0
    for i in range(R):
        for j in range(C):
            if dust_room[i][j] > 0:
                total_fd += dust_room[i][j]

    return total_fd

up, down = air_cleaners
for _ in range(T):
    room = diffuse(room)
    room = rotate(room, 1, up)
    room = rotate(room, -1, down)
print(total_fine_dust(room))