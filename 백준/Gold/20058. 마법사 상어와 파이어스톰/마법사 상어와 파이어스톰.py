from copy import deepcopy
from collections import deque
N, Q = map(int, input().split())

matrix_len = pow(2, N)
matrix = [None for _ in range(matrix_len)]

for i in range(matrix_len):
    matrix[i] = list(map(int, input().split()))

L_list = list(map(int, input().split()))

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def rotation(L: int, matrix):
    step = 2 ** L
    new_matrix = [[0] * matrix_len for _ in range(matrix_len)]
    
    for y in range(0, matrix_len, step):
        for x in range(0, matrix_len, step):
            for i in range(step):
                for j in range(step):
                    new_matrix[y + j][x + step - i - 1] = matrix[y + i][x + j]

    return new_matrix


def is_melt(y, x):
    if matrix[y][x] == 0:
        return False

    neighbor_ice = 0
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0 <= ny < matrix_len and 0 <= nx < matrix_len and matrix[ny][nx] != 0:
            neighbor_ice += 1

    if neighbor_ice < 3:
        return True
    else:
        return False


def melt_ice():
    melted_ice = []
    for y in range(matrix_len):
        for x in range(matrix_len):
            if is_melt(y, x):
                melted_ice.append([y, x])
    for y, x in melted_ice:
        matrix[y][x] -= 1


def bfs():
    visit = [[False for _ in range(matrix_len)] for _ in range(matrix_len)]
    max_size = 0
    for i in range(matrix_len):
        for j in range(matrix_len):
            size = 0
            if not visit[i][j] and matrix[i][j] > 0:
                deq = deque([[i, j]])
                visit[i][j] = True
                while deq:
                    y, x = deq.popleft()
                    size += 1
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < matrix_len and 0 <= nx < matrix_len:
                            if not visit[ny][nx] and matrix[ny][nx] != 0:
                                visit[ny][nx] = True
                                deq.append([ny, nx])
            max_size = max(size, max_size)
    return max_size
            


for L in L_list:
    if L != 0:
        matrix = deepcopy(rotation(L, matrix))
    melt_ice()


print(sum(map(sum, matrix)))
print(bfs())