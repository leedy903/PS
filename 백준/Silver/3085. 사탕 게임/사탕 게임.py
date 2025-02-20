import sys
from collections import deque
input = sys.stdin.readline

def get_longest():
    max_length = 0
    for i in range(n):
        for j in range(n):
            candy = matrix[i][j]

            length = 1
            deq = deque([[i, j]])
            while deq:
                y, x = deq.popleft()
                ny = y + 1
                if 0 <= ny < n and candy == matrix[ny][x]:
                    length += 1
                    deq.append([ny, x])
            max_length = max(length, max_length)

            length = 1
            deq = deque([[i, j]])
            while deq:
                y, x = deq.popleft()
                nx = x + 1
                if 0 <= nx < n and candy == matrix[y][nx]:
                    length += 1
                    deq.append([y, nx])
            max_length = max(length, max_length)
    return max_length


n = int(input())
matrix = [list(input().strip()) for _ in range(n)]

longest = 0
for i in range(n):
    for j in range(n):
        if i + 1 < n and matrix[i][j] != matrix[i + 1][j]:
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
            longest = max(longest, get_longest())
            matrix[i][j], matrix[i + 1][j] = matrix[i + 1][j], matrix[i][j]
        if j + 1 < n and matrix[i][j] != matrix[i][j + 1]:
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]
            longest = max(longest, get_longest())
            matrix[i][j], matrix[i][j + 1] = matrix[i][j + 1], matrix[i][j]

print(longest)