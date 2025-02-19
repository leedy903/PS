N = int(input())
matrix = [None for _ in range(N)]

for i in range(N):
    matrix[i] = list(map(int, input().split()))

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

blow_sands = [[[1, 0, 7], [-1, 0, 7], [2, 0, 2], [-2, 0, 2], [-1, -1, 10], [1, -1, 10], [-1, 1, 1], [1, 1, 1], [0, -2, 5]],
                [[0, -1, 7], [0, 1, 7], [0, -2, 2], [0, 2, 2], [1, -1, 10], [1, 1, 10], [-1, -1, 1], [-1, 1, 1], [2, 0, 5]],
                [[-1, 0, 7], [1, 0, 7], [2, 0, 2], [-2, 0, 2], [1, 1, 10], [-1, 1, 10], [-1, -1, 1], [1, -1, 1], [0, 2, 5]],
                [[0, -1, 7], [0, 1, 7], [0, -2, 2], [0, 2, 2], [-1, -1, 10], [-1, 1, 10], [1, -1, 1], [1, 1, 1], [-2, 0, 5]]]

out_sand = 0
moving_direction = 0
moving_distance = 1
ty, tx = N // 2, N // 2

while True:
    for i in range(1, moving_distance + 1):
        ty += dy[moving_direction]
        tx += dx[moving_direction]
        if tx == -1:
            break
        sand = matrix[ty][tx]
        alpha_sand = sand
        for blow_sand in blow_sands[moving_direction]:
            sy, sx, sw = blow_sand
            ny = ty + sy
            nx = tx + sx
            blow_sand = (sand * sw) // 100
            alpha_sand -= blow_sand
            if 0 <= ny < N and 0 <= nx < N:
                matrix[ny][nx] += blow_sand
            else:
                out_sand += blow_sand
        ay = ty + dy[moving_direction]
        ax = tx + dx[moving_direction]
        if 0 <= ay < N and 0 <= ax < N:
            matrix[ay][ax] += alpha_sand
        else:
            out_sand += alpha_sand

        matrix[ty][tx] = 0


    moving_direction = (moving_direction + 1) % 4
    if moving_direction % 2 == 0:
        moving_distance += 1

    if ty == 0 and tx == -1:
        break

print(out_sand)