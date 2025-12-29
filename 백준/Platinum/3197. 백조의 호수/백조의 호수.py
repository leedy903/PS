import sys
from collections import deque

input = sys.stdin.readline

def find_parent(x):
    if x != parents[x]:
        parents[x] = find_parent(parents[x])
    return parents[x]

def unoin(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parents[b] = a
    else:
        parents[a] = b

answer = 1
R, C = map(int, input().split())
matrix = [list(input().strip()) for _ in range(R)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

visited = [[False for _ in range(C)] for _ in range(R)]
parents = [i for i in range(R * C)]
boarder_line = set()
swans = []

for y in range(R):
    for x in range(C):
        if matrix[y][x] == 'L':
            swans.append([y, x])
        if not visited[y][x] and matrix[y][x] in ('.', 'L'):
            visited[y][x] = True
            deq = deque([[y, x]])
            while deq:
                cy, cx = deq.popleft()
                for i in range(4):
                    ny = cy + dy[i]
                    nx = cx + dx[i]
                    if 0 <= ny < R and 0 <= nx < C and not visited[ny][nx]:
                        if matrix[ny][nx] in ('.', 'L'):
                            cur_id = find_parent(cy * C + cx)
                            next_id = find_parent(ny * C + nx)
                            unoin(cur_id, next_id)
                            visited[ny][nx] = True
                            deq.append([ny, nx])
                        if matrix[ny][nx] == 'X':
                            boarder_line.add((cy, cx))

boarder_line = deque(list(boarder_line)[:])

for day in range(1, R * C + 1):
    next_boarder_line = set()
    while boarder_line:
        y, x = boarder_line.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if matrix[ny][nx] == 'X':
                    next_boarder_line.add((ny, nx))

    next_boarder_line = list(next_boarder_line)

    for y, x in next_boarder_line:
        matrix[y][x] = '.'

    for y, x in next_boarder_line:
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < R and 0 <= nx < C:
                if matrix[ny][nx] in ('.', 'L'):
                    cur_id = find_parent(y * C + x)
                    next_id = find_parent(ny * C + nx)
                    unoin(cur_id, next_id)

    s1 = swans[0]
    s2 = swans[1]
    s1_id = find_parent(s1[0] * C + s1[1])
    s2_id = find_parent(s2[0] * C + s2[1])
    
    if s1_id == s2_id:
        answer = day
        break

    boarder_line = deque(next_boarder_line[:])

print(answer)