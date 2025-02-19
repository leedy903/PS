import sys
r, c, k = map(int, sys.stdin.readline().split())

matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

def operation(matrix: list, row_size: int, column_size: int) -> list:
    if row_size < column_size:
        matrix = [list(x) for x in zip(*matrix)]
    # R operation
    max_row_len = 0
    for i, row in enumerate(matrix):
        row_count = dict()
        for value in row:
            if value == 0:
                continue
            if value in row_count:
                row_count[value] += 1
            else:
                row_count[value] = 1
        sorted_row = sorted(row_count.items(), key = lambda item: (item[1], item[0]))
        new_row = []
        for k, v in sorted_row:
            new_row.append(k)
            new_row.append(v)
        matrix[i] = new_row[:100]
        max_row_len = max(max_row_len, len(new_row))

    for i, row in enumerate(matrix):
        surplus_zero = [0] * (max_row_len - len(row))
        matrix[i] += surplus_zero

    if row_size < column_size:
        matrix = [list(x) for x in zip(*matrix)]
    
    return matrix

for T in range(101):
    row_size = len(matrix)
    column_size = len(matrix[0])
    
    if r <= row_size and c <= column_size:
        if matrix[r - 1][c - 1] == k:
            print(T)
            break
            
    matrix = operation(matrix, row_size, column_size)
else:
    print(-1)