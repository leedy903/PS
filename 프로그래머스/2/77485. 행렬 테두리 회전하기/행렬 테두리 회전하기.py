from collections import deque

def solution(rows, columns, queries):
    answer = []
    matrix = [[] for _ in range(rows)]
    for i in range(rows):
        matrix[i] = list(range((columns * i) + 1, (columns * (i + 1)) + 1))
    
    for query in queries:
        y1, x1, y2, x2 = query
        rotate_deq = deque()
        
        # Copy
        for i in range(x1 - 1, x2 - 1):
            rotate_deq.append(matrix[y1 - 1][i])
        for i in range(y1 - 1, y2 - 1):
            rotate_deq.append(matrix[i][x2 - 1])
        for i in range(x2 - 1, x1 - 2, -1):
            rotate_deq.append(matrix[y2 - 1][i])
        for i in range(y2 - 2, y1 - 1, -1):
            rotate_deq.append(matrix[i][x1 - 1])
            
        # Rotate and Choose Min
        rotate_deq.rotate()
        answer.append(min(rotate_deq))
        
        # Paste
        j = 0
        for i in range(x1 - 1, x2 - 1):
            matrix[y1 - 1][i] = rotate_deq[j]
            j += 1
        for i in range(y1 - 1, y2 - 1):
            matrix[i][x2 - 1] = rotate_deq[j]
            j += 1
        for i in range(x2 - 1, x1 - 2, -1):
            matrix[y2 - 1][i] = rotate_deq[j]
            j += 1
        for i in range(y2 - 2, y1 - 1, -1):
            matrix[i][x1 - 1] = rotate_deq[j]
            j += 1        
    
    return answer