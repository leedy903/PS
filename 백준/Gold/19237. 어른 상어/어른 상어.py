from collections import deque
N, M, K = map(int, input().split())

matrix = [None for _ in range(N)]
smell_matrix = [[[0, 0] for _ in range(N)] for _ in range(N)]
sharks = deque([None for _ in range(M)])
sharks_priorities = [[] for _ in range(M)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        now = row[j]
        if now != 0:
            sharks[now - 1] = [i, j]
    matrix[i] = row

sharks_directions = list(map(int, input().split()))
for i in range(M):
    sharks_directions[i] -= 1

for i in range(M):
    for j in range(4):
        u, d, l, r = map(int, input().split())
        sharks_priorities[i].append(list([u - 1, d - 1, l - 1, r - 1]))


def get_next_point(y, x):
    movable_point, self_smell_point = [], []
    shark_num = matrix[y][x]
    sd = sharks_directions[shark_num - 1]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < N and 0 <= nx < N:
            if smell_matrix[ny][nx][0] == 0:
                movable_point.append([ny, nx, i])
            if smell_matrix[ny][nx][0] == shark_num:
                self_smell_point.append([ny, nx, i])

    if len(movable_point) == 0:
        movable_point = self_smell_point
    
    if len(movable_point) > 1:
        for i in range(4):
            nsd = sharks_priorities[shark_num - 1][sd][i]
            ny = y + dy[nsd]
            nx = x + dx[nsd]
            if 0 <= ny < N and 0 <= nx < N and [ny, nx, nsd] in movable_point:
                sharks_directions[shark_num - 1] = nsd
                return [ny, nx]
    else:
        ny, nx, nsd = movable_point[0]
        sharks_directions[shark_num - 1] = nsd
        return [ny, nx]
        

def diffues_and_decrease_smell():
    for y in range(N):
        for x in range(N):
            if smell_matrix[y][x][0] != 0:
                smell_matrix[y][x][1] -= 1
                if smell_matrix[y][x][1] == 0:
                    smell_matrix[y][x][0] = 0
            shark_num = matrix[y][x]
            if shark_num != 0:
                smell_matrix[y][x]= [shark_num, K]


def sharks_move():
    while sharks:

        shark = sharks.popleft()
        if shark:
            y, x = shark
            ny, nx = get_next_point(y, x)

            if matrix[ny][nx] == 0:
                matrix[ny][nx] = matrix[y][x]
            else:
                matrix[ny][nx] = min(matrix[ny][nx], matrix[y][x])
            matrix[y][x] = 0
    

def get_sharks():
    sharks = deque([None for _ in range(M)])
    for y in range(N):
        for x in range(N):
            now = matrix[y][x]
            if now != 0:
                sharks[now - 1] = [y, x]
    return sharks


def check_end():
    for i, shark in enumerate(sharks):
        if i != 0 and shark:
            return False
    return True


for i in range(1, 1001):
    diffues_and_decrease_smell()
    sharks_move()
    sharks = get_sharks()
    if check_end() == 1:
        print(i)
        break
else:
    print(-1)

