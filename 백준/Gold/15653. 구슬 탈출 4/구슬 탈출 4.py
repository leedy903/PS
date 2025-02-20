import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

def move(bead, d):
    y, x = bead
    while True:
        y += dy[d]
        x += dx[d]
        if matrix[y][x] == 'O':
            break
        if matrix[y][x] == '#':
            y -= dy[d]
            x -= dx[d]
            break
    return [y, x]

def bfs():
    while deq:
        red, blue, count = deq.popleft()

        ry, rx = red
        by, bx = blue
        for d in range(4):
            new_red = move(red, d)
            new_blue = move(blue, d)

            nry, nrx = new_red
            nby, nbx = new_blue

            if matrix[nby][nbx] == 'O':
                continue
            if matrix[nry][nrx] == 'O':
                return count
            
            if new_red == new_blue:
                if abs(nry - ry) + abs(nrx - rx) > abs(nby - by) + abs(nbx - bx):
                    nry -= dy[d]
                    nrx -= dx[d]
                else:
                    nby -= dy[d]
                    nbx -= dx[d]

            if not visited[nry][nrx][nby][nbx]:
                visited[nry][nrx][nby][nbx] = True
                deq.append([[nry, nrx], [nby, nbx], count + 1])
        count += 1
    return -1

n, m = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(n)]
visited = [[[[False for _ in range(m)] for _ in range(n)] for _ in range(m)] for _ in range(n)]

red = []
blue = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'R':
            red = [i, j]
        if matrix[i][j] == 'B':
            blue = [i, j]

ry, rx = red
by, bx = blue
deq = deque([[red, blue, 1]])
visited[ry][rx][by][bx] = True
ans = bfs()
print(ans)