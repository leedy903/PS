from collections import deque
from copy import deepcopy
N, M = map(int, input().split())

matrix = [None for _ in range(N)]

for i in range(N):
    matrix[i] = list(map(int, input().split()))

score = 0

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]


def get_groups():
    visit = [[False for _ in range(N)] for _ in range(N)]
    groups = []

    for i in range(N):
        for j in range(N):
            if not visit[i][j] and matrix[i][j] > 0:
                group = [[i, j]]
                group_num = matrix[i][j]
                zeros = []
                visit[i][j] = True
                deq = deque([[i, j]])
                while deq:
                    y, x = deq.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx]:
                            if matrix[ny][nx] == group_num:
                                visit[ny][nx] = True
                                deq.append([ny, nx])
                                group.append([ny, nx])

                            if matrix[ny][nx] == 0:
                                visit[ny][nx] = True
                                deq.append([ny, nx])
                                group.append([ny, nx])
                                zeros.append([ny, nx])

                for zy, zx in zeros:
                    visit[zy][zx] = False
                
                if len(group) > 1:
                    groups.append(group)
    
    groups.sort(key = lambda x : len(x), reverse = True)
    return groups


def get_biggest_group(groups):
    biggest_group = []
    groups = [group for group in groups if len(group) == len(groups[0])]
    
    if len(groups) > 1:
        zero_count = [0 for _ in range(len(groups))]
        for i, group in enumerate(groups):
            for y, x in group:
                if matrix[y][x] == 0:
                    zero_count[i] += 1
        max_zero = max(zero_count)
        groups = [group for i, group in enumerate(groups) if zero_count[i] == max_zero]

    if len(groups) > 1:
        standards = [[i, group[0]] for i, group in enumerate(groups)]
        standards.sort(key = lambda x : (-x[1][0], -x[1][1]))
        groups = [groups[standards[0][0]]]

    biggest_group = groups[0]

    return biggest_group


def remove_group(group):
    for y, x in group:
        matrix[y][x] = -2


def gravity_rightahead():
    for y in range(N):
        index = 0
        new_sections = []
        while index < N:
            if matrix[y][index] == -1:
                new_sections += [-1]
                index += 1
            else:
                section = []
                while matrix[y][index] != -1:
                    section.append(matrix[y][index])
                    index += 1
                    if index > N - 1:
                        break

                block_section = []
                for block in section:
                    if block != -2:
                        block_section.append(block)
                new_sections += [-2] * (len(section) - len(block_section)) + block_section
            
        matrix[y] = new_sections
        

def counterwise_rotation():
    temp_matrix = deepcopy(matrix)
    for y in range(N):
        for x in range(N):
            matrix[(N - 1) - x][y] = temp_matrix[y][x]


def clockwise_rotation():    
    temp_matrix = deepcopy(matrix)
    for y in range(N):
        for x in range(N):
            matrix[x][(N - 1) - y] = temp_matrix[y][x]


def auto_play(groups):
    global score
    group = get_biggest_group(groups)
    score += len(group) ** 2
    remove_group(group)
    counterwise_rotation()
    gravity_rightahead()
    counterwise_rotation()
    gravity_rightahead()
    clockwise_rotation()

groups = get_groups()
while groups != []:
    auto_play(groups)
    groups = get_groups()

print(score)

