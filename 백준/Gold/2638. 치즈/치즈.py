import sys
from collections import deque
input = sys.stdin.readline

def is_empty():
    return sum(map(sum, matrix)) == 0

dy = [-1, 0, 1, 0]
dx =[0, -1, 0, 1]

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

time = 0
while not is_empty():
    time += 1
    visit = [[0 for _ in range(m)] for _ in range(n)]
    count_matrix = [[0 for _ in range(m)] for _ in range(n)]
    deq = deque([[0, 0]])
    visit[0][0] = True
    while deq:
        y, x = deq.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if matrix[ny][nx] == 0 and not visit[ny][nx]:
                    deq.append([ny, nx])
                    visit[ny][nx] = True
                else:
                    count_matrix[ny][nx] += 1
    for i in range(n):
        for j in range(m):
            if count_matrix[i][j] >= 2:
                matrix[i][j] = 0
    
print(time)