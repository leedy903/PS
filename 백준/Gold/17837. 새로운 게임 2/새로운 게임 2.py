import sys
input = sys.stdin.readline

switch = [1, -1]
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
matrix = [[[] for _ in range(n)] for _ in range(n)]
pieces = []
for i in range(k):
    y, x, d = map(int, input().split())
    pieces.append([y - 1, x - 1, d - 1])

def init_game():
     for i, piece in enumerate(pieces):
        y, x, _ = piece
        matrix[y][x].append(i)

def move(piece_id, count):
    y, x, d = pieces[piece_id]
    ny = y + dy[d]
    nx = x + dx[d]

    if 0 <= ny < n and 0 <= nx < n and board[ny][nx] < 2:
        cur_idx = matrix[y][x].index(piece_id)
        companies = matrix[y][x][cur_idx:]
        if board[ny][nx] == 1:
            companies.reverse()
        matrix[y][x] = matrix[y][x][:cur_idx]
        matrix[ny][nx].extend(companies)
        for company in companies:
            pieces[company][0] = ny
            pieces[company][1] = nx
    else:
        if count > 1:
            return
        else:
            pieces[piece_id][2] = d + switch[d % 2]
            move(piece_id, count + 1)

def is_4_stack():
    for i in range(n):
        for j in range(n):
            if len(matrix[i][j]) >= 4:
                   return True
    return False


init_game()

for turn in range(1, 1001):
    is_finish = False
    for piece_id in range(len(pieces)):
        move(piece_id, 1)
        if is_4_stack():
            is_finish = True
            break
    if is_finish:
        print(turn)
        break
else:
    print(-1)