def solution(board):
    answer = 1
    n = len(board)
    m = len(board[0])
    
    for y in range(1, n):
        for x in range(1, m):
            if board[y][x] != 0:
                board[y][x] = min(board[y - 1][x - 1], board[y - 1][x], board[y][x - 1]) + 1
                
    max_length = max(map(max, board))
    answer = max_length * max_length
    
    return answer