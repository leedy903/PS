from collections import deque
N = int(input())
matrix = [list(input()) for _ in range(N)]

def get_district_number(matrix: list) -> int:
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]

    visited = [[False for _ in range(N)] for _ in range(N)]
    district_number = 0
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                district_number += 1
                color = matrix[i][j]
                visited[i][j] = True
                deq = deque([[i, j]])
                while deq:
                    y, x = deq.popleft()
                    for k in range(4):
                        ny = y + dy[k]
                        nx = x + dx[k]
                        if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and matrix[ny][nx] == color:
                            deq.append([ny, nx])
                            visited[ny][nx] = True
    return district_number

normal_district_number = get_district_number(matrix)

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 'R':
            matrix[i][j] = 'G'

red_green_color_weakness_disctrict_number = get_district_number(matrix)

print(normal_district_number, red_green_color_weakness_disctrict_number)