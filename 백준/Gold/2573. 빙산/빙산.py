from collections import deque

N, M = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]

meltCount = 0

while True:

    # 빙산 녹이기
    melt_matrix = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if matrix[y][x] != 0 and not visited[y][x]:
                visited[y][x] = True
                coast = 0
                for i in range(4):
                    ny = y + dy[i]
                    nx = x + dx[i]
                    if 0 <= ny < N and 0 <= nx < M and matrix[ny][nx] == 0:
                            coast += 1
                melt_matrix[y][x] = max(matrix[y][x] - coast, 0)

    # 새로운 빙산 맵으로 변경
    for i in range(N):
        matrix[i] = melt_matrix[i][:]
    
    meltCount += 1

    #  분리된 빙산 구하기
    splitCount = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for y in range(N):
        for x in range(M):
            if matrix[y][x] != 0 and not visited[y][x]:
                splitCount += 1
                visited[y][x] = True
                deq = deque([[y, x]])
                while deq:
                    now_y, now_x = deq.popleft()
                    for i in range(4):
                        ny = now_y + dy[i]
                        nx = now_x + dx[i]
                        if 0 <= ny < N and 0 <= nx < M:
                            if matrix[ny][nx] != 0 and not visited[ny][nx]:
                                visited[ny][nx] = True
                                deq.append([ny, nx])

    if splitCount > 1:
        break

    elif splitCount == 0:
        meltCount = 0
        break

print(meltCount)