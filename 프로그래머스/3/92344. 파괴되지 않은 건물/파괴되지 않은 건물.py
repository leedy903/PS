def solution(board, skill):
    answer = 0
    n, m = len(board), len(board[0])
    prefix_sum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for t, r1, c1, r2, c2, d in skill:
        if t == 1:
            d = -d
        prefix_sum[r1][c1] += d
        prefix_sum[r1][c2 + 1] += -d
        prefix_sum[r2 + 1][c1] += -d
        prefix_sum[r2 + 1][c2 + 1] += d
        
    for y in range(n + 1):
        for x in range(m):
            prefix_sum[y][x + 1] += prefix_sum[y][x]
            
    for y in range(n):
        for x in range(m + 1):
            prefix_sum[y + 1][x] += prefix_sum[y][x]
    
    for y in range(n):
        for x in range(m):
            board[y][x] += prefix_sum[y][x]
    
    for y in range(n):
        for x in range(m):
            if board[y][x] > 0:
                answer += 1
                    
    return answer