def solution(board):
    def is_won(player):
        for i in range(3):
            if (board[i][0] == board[i][1] == board[i][2] == player) or (board[0][i] == board[1][i] == board[2][i] == player):
                return True
        if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False
    answer = 1
    o_cnt = 0
    x_cnt = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                o_cnt += 1
            elif board[i][j] == 'X':
                x_cnt += 1
    
    o_win = is_won('O')
    x_win = is_won('X')
    if not (o_cnt == x_cnt or o_cnt == x_cnt + 1):
        answer = 0
    if o_win and x_win:
        answer = 0
    if o_win and o_cnt != x_cnt + 1:
        answer = 0
    if x_win and o_cnt != x_cnt:
        answer = 0
    return answer