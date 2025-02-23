from collections import deque

dy = [1, 0, -1]
dx = [0, 1, -1]

def solution(n):
    answer = []
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    deq = deque([[0, 0, 0]])
    matrix[0][0] = 1
    while deq:
        y, x, d = deq.popleft()
        ny = y + dy[d]
        nx = x + dx[d]
        
        if (0 <= ny < n and 0 <= nx < n) and matrix[ny][nx] == 0:
            matrix[ny][nx] = matrix[y][x] + 1
            deq.append([ny, nx, d])
        else:
            nd = (d + 1) % 3
            ny = y + dy[nd]
            nx = x + dx[nd]
            if (0 <= ny < n and 0 <= nx < n) and matrix[ny][nx] == 0:
                matrix[ny][nx] = matrix[y][x] + 1
                deq.append([ny, nx, nd])
        
    for y in range(n):
        for x in range(n):
            if matrix[y][x] != 0:
                answer.append(matrix[y][x])
    
    return answer