from copy import deepcopy
from collections import deque

fdy = [0, -1, -1, -1, 0, 1, 1, 1]
fdx = [-1, -1, 0, 1, 1, 1, 0, -1]
sdy = [-1, 0, 1, 0]
sdx = [0, -1, 0, 1]


def spell_practice(S):
    for i in range(S):

        copy_fish()
        fish_move()
        smell_decrease()
        shark_move()
        paste_fish()


def copy_fish():
    global respawn_fishes
    for y in range(4):
        for x in range(4):
            for fish in fish_board[y][x]:
                respawn_fishes.append([y, x, fish])


def fish_move():
    global fish_board
    new_fish_board = [[[] for _ in range(4)] for _ in range(4)]
    for y in range(4):
        for x in range(4):
            fishes = fish_board[y][x]
            for fish in fishes:
                for i in range(fish + 8, fish, -1):
                    d = i % 8
                    ny = y + fdy[d]
                    nx = x + fdx[d]

                    if 0 <= ny < 4 and 0 <= nx < 4:
                        if (ny != sy or nx != sx) and smell_board[ny][nx] == 0:
                            new_fish_board[ny][nx].append(d)
                            break
                else:
                    new_fish_board[y][x].append(fish)
    fish_board = deepcopy(new_fish_board)


def smell_decrease():
    global smell_board
    for y in range(4):
        for x in range(4):
            if smell_board[y][x] > 0:
                smell_board[y][x] -= 1
            


def shark_move():
    global fish_board, smell_board, best_route, sy, sx, max_eat
    visit = [[False for _ in range(4)] for _ in range(4)]
    set_shark_best_route(0, sy, sx, 0, visit, [])
    

    for d in best_route:
        sy += sdy[d]
        sx += sdx[d]

        if len(fish_board[sy][sx]) > 0:
            fish_board[sy][sx] = []
            smell_board[sy][sx] = 2
    
    max_eat = -1


def set_shark_best_route(depth, y, x, eat_count, visit, route):
    global max_eat, best_route
    if depth == 3:
        if max_eat < eat_count:
            max_eat = eat_count
            best_route = route[:]
        return
    
    for nd in range(4):
        ny = y + sdy[nd]
        nx = x + sdx[nd]
        if 0 <= ny < 4 and 0 <= nx < 4:
            if not visit[ny][nx]:
                visit[ny][nx] = True
                set_shark_best_route(depth + 1, ny, nx, eat_count + len(fish_board[ny][nx]), visit, route + [nd])
                visit[ny][nx] = False
            else:
                set_shark_best_route(depth + 1, ny, nx, eat_count, visit, route + [nd])

    return


def paste_fish():
    global respawn_fishes
    while respawn_fishes:
        y, x, d = respawn_fishes.popleft()
        fish_board[y][x].append(d)


def count_fish():
    global fish_board
    total_fish = 0
    for y in range(4):
        for x in range(4):
            total_fish += len(fish_board[y][x])

    return total_fish


M, S = map(int, input().split())
respawn_fishes = deque([None for _ in range(M)])

for i in range(M):
    y, x, d = map(int, input().split())
    respawn_fishes[i] = [y - 1, x - 1, d - 1]

sy, sx = map(int, input().split())
sy, sx = sy - 1, sx - 1

max_eat = -1
best_route = []
fish_board = [[[] for _ in range(4)] for _ in range(4)]
smell_board = [[0 for _ in range(4)] for _ in range(4)]


paste_fish()
spell_practice(S)
print(count_fish())