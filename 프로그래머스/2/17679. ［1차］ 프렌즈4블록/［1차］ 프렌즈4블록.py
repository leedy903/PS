from collections import deque
def solution(m, n, board):
    answer = 0
    
    print(*board)
    
    for b in zip(*board):
        print(b)
    
    board = list(map(list, zip(*board)))
    
    while True:
        remove_set = set()
        for i in range(n - 1):
            for j in range(m - 1):
                if board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][j + 1] != '-':
                    remove_set |= set([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])
        
        if len(remove_set) == 0:
             break
                
        answer += len(remove_set)
        
        for x, y in remove_set:
            board[x][y] = '-'
        
        for i, row in enumerate(board):
            bar = ['-'] * row.count('-')
            remain = [block for block in row if block != '-']
            board[i] = bar + remain
        
        
    return answer