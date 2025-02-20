from collections import deque
import sys
input = sys.stdin.readline

dy = [[-1, 0, 1, 1, 0, -1], [-1, 0, 1, 1, 0, -1]]
dx = [[-1, -1, -1, 0, 1, 0], [0, -1, 0, 1, 1, 1]]

w, h = map(int, input().split())
matrix = [[0 for _ in range(w + 2)] for _ in range(h + 2)]
for i in range(1, h + 1):
    matrix[i][1 : w + 1] = list(map(int, input().split()))
visited = [[False for _ in range(w + 2)] for _ in range(h + 2)]

answer = 0
deq = deque([[0, 0]])
visited[0][0] = True
while deq:
    y, x = deq.popleft()
    mode = y % 2
    for k in range(6):
        ny = y + dy[mode][k]
        nx = x + dx[mode][k]
        if 0 <= ny < h + 2 and 0 <= nx < w + 2:
            if matrix[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                deq.append([ny, nx])
            elif matrix[ny][nx] == 1:
                answer += 1

print(answer)