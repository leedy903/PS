from collections import deque

def is_connected(fsp):
    visited = [[True for _ in range(5)] for _ in range(5)]

    for y, x in fsp:
        visited[y][x] = False

    fy, fx = fsp[0]
    deq = deque([[fy, fx]])
    visited[fy][fx] = True

    princess = 1

    while deq:
        y, x = deq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < 5 and 0 <= nx < 5 and not visited[ny][nx]:
                visited[ny][nx] = True
                princess += 1
                deq.append([ny, nx])

    return princess == 7


def dfs(depth, start, y_count):
    global count

    if y_count >= 4:
        return
    
    if depth == 7:
        if is_connected(fsp):
            count += 1
        return

    for i in range(start, 25):
        y = i // 5
        x = i % 5

        temp_y_count = 0
        if matrix[y][x] == 'Y':
            temp_y_count = 1

        fsp.append([y, x])
        dfs(depth + 1, i + 1, y_count + temp_y_count)
        fsp.pop()


dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

fsp = []
count = 0

matrix = [list(input()) for _ in range(5)]

dfs(0, 0, 0)

print(count)