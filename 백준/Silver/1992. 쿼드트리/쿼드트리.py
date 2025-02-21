import sys
input = sys.stdin.readline

n = int(input())
matrix =  [list(input().strip()) for _ in range(n)]

dy = [0, 0, 1, 1]
dx = [0, 1, 0, 1]

def quad_compression(step, y, x):
    if step == 0:
        return matrix[y][x]

    data = []
    for i in range(4):
        ny = y + dy[i] * step
        nx = x + dx[i] * step
        data.append(quad_compression(step // 2, ny, nx))

    if is_compressible(data):
        return data[0]
    else:
        return '(' + ''.join(data) + ')'

def is_compressible(data):
    return is_match(data, '0') or is_match(data, '1')

def is_match(data, key):
    for i in range(4):
        if data[i] != key:
            return False
    return True

answer = quad_compression(n // 2, 0, 0)
print(answer)
