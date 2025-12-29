from collections import deque
import sys
input = sys.stdin.readline

def solve():
    R, C = map(int, input().split())
    lake = [list(input().rstrip()) for _ in range(R)]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    water_q = deque()
    swans = []

    for y in range(R):
        for x in range(C):
            if lake[y][x] != 'X':
                water_q.append((y, x))
            if lake[y][x] == 'L':
                swans.append((y, x))

    sy, sx = swans[0]
    ty, tx = swans[1]

    swan_q = deque([(sy, sx)])
    next_swan_q = deque()

    water_visited = [[False]*C for _ in range(R)]
    swan_visited = [[False]*C for _ in range(R)]

    water_visited[sy][sx] = True
    swan_visited[sy][sx] = True

    day = 0

    while True:
        while swan_q:
            y, x = swan_q.popleft()
            if (y, x) == (ty, tx):
                print(day)
                return

            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < R and 0 <= nx < C and not swan_visited[ny][nx]:
                    swan_visited[ny][nx] = True
                    if lake[ny][nx] == 'X':
                        next_swan_q.append((ny, nx))
                    else:
                        swan_q.append((ny, nx))

        next_water_q = deque()
        while water_q:
            y, x = water_q.popleft()
            for d in range(4):
                ny, nx = y + dy[d], x + dx[d]
                if 0 <= ny < R and 0 <= nx < C and not water_visited[ny][nx]:
                    water_visited[ny][nx] = True
                    if lake[ny][nx] == 'X':
                        lake[ny][nx] = '.'
                        next_water_q.append((ny, nx))
                    else:
                        water_q.append((ny, nx))

        swan_q = next_swan_q
        water_q = next_water_q
        next_swan_q = deque()

        day += 1

if __name__ == "__main__":
    solve()