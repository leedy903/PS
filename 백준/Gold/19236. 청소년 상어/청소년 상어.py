from copy import deepcopy
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

matrix = [None for _ in range(4)]

for i in range(4):
    info = list(map(int, input().split()))
    row = []    
    for j in range(4):
        row.append([info[j * 2], info[j * 2 + 1] - 1])    
    matrix[i] = row


def get_fish_location(matrix: list, fish_num: int) -> list:
    for i in range(4):
        for j in range(4):
            if matrix[i][j][0] == fish_num:
                return [i, j]
    

def fish_move(matrix: list) -> None:
    for fish_num in range(1, 17):
        fish_location = get_fish_location(matrix, fish_num)
        if fish_location:
            fy, fx = fish_location
            fd = matrix[fy][fx][1]

            for i in range(fd, fd + 8):
                direction = i % 8
                ny = fy + dy[direction]
                nx = fx + dx[direction]

                if 0 <= ny < 4 and 0 <= nx < 4 and matrix[ny][nx][0] != 99:
                    matrix[fy][fx][1] = direction
                    matrix[ny][nx], matrix[fy][fx] = matrix[fy][fx], matrix[ny][nx]
                    break


def get_prey_fishes(matrix: list, sy: int, sx: int):
    prey_fishes = []
    ny, nx = sy, sx
    sd = matrix[sy][sx][1]
    for i in range(4):
        ny += dy[sd]
        nx += dx[sd]
        if 0 <= ny < 4 and 0 <= nx < 4 and matrix[ny][nx][0] != 0:
            prey_fishes.append([ny, nx, matrix[ny][nx][0]])
    
    return prey_fishes


def dfs(matrix: list, sy: int, sx: int, score: int):
    global max_score
    max_score = max(score, max_score)

    next_matrix = deepcopy(matrix)
    next_matrix[sy][sx][0] = 99

    fish_move(next_matrix)
    
    prey_fishes = get_prey_fishes(next_matrix, sy, sx)

    if len(prey_fishes) == 0:
        return

    next_matrix[sy][sx][0] = 0
    for py, px, pn in prey_fishes:
        dfs(next_matrix, py, px, score + pn)

score = matrix[0][0][0]
sy, sx = 0, 0
max_score = 0

dfs(matrix, sy, sx, score)
print(max_score)