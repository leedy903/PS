import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
min_height = min(map(min, matrix))
max_height = max(map(max, matrix))
time, height = float('inf'), 0
for h in range(min_height, max_height + 1):
    work_time = 0
    extra_block = b
    for i in range(n):
        for j in range(m):
            gap = abs(matrix[i][j] - h)
            if matrix[i][j] < h:
                extra_block -= gap
                work_time += gap
            elif matrix[i][j] > h:
                extra_block += gap
                work_time += 2 * gap
    
    if extra_block >= 0 and time >= work_time:
        time = work_time
        height = h
print(time, height)