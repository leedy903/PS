from collections import deque
N, M, K = map(int, input().split())
matrix = [[deque([]) for _ in range(N)] for _ in range(N)]
fireballs = deque([[] for _ in range(M)])

for i in range(M):
    y, x, m, s, d = list(map(int, input().split()))
    fireballs[i] = [y - 1, x - 1, m, s, d]

dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]


def spell_fireball():
    move_fireball()
    update_fireballs()


def move_fireball():
    while fireballs:
        y, x, m, s, d = fireballs.popleft()
        ny = (y + dy[d] * s) % N
        nx = (x + dx[d] * s) % N
        matrix[ny][nx].append([m, s, d])


def update_fireballs():
    for y in range(N):
        for x in range(N):
            fireballs_num = len(matrix[y][x])
            if fireballs_num > 1:
                sum_mass, sum_speed, next_direction, odd_directions, even_directions = 0, 0, 0, 0, 0
                while matrix[y][x]:
                    m, s, d = matrix[y][x].popleft()
                    sum_mass += m
                    sum_speed += s
                    if d % 2 != 0:
                        odd_directions += 1
                    else:
                        even_directions += 1
                if odd_directions != fireballs_num and even_directions != fireballs_num:
                    next_direction = 1
                if sum_mass // 5:
                    for i in range(4):
                        fireballs.append([y, x, sum_mass // 5, sum_speed // fireballs_num, next_direction + i * 2])

            if fireballs_num == 1:
                m, s, d = matrix[y][x].popleft()
                fireballs.append([y, x, m, s, d])


def get_fireballs_mass():
    return sum([fireball[2] for fireball in fireballs])


for i in range(K):
    spell_fireball()

print(get_fireballs_mass())