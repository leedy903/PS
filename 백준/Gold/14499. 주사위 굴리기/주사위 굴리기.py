import sys, copy
N, M, x, y, K = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
directions = list(map(int, sys.stdin.readline().split()))

dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def roll(direc: int) -> None:
    temp_dice = copy.deepcopy(dice)    
    if direc == 1:
        dice[1] = temp_dice[4]
        dice[4] = temp_dice[6]
        dice[6] = temp_dice[3]
        dice[3] = temp_dice[1]
    elif direc == 2:
        dice[4] = temp_dice[1]
        dice[6] = temp_dice[4]
        dice[3] = temp_dice[6]
        dice[1] = temp_dice[3]
    elif direc == 3:
        dice[1] = temp_dice[5]
        dice[5] = temp_dice[6]
        dice[6] = temp_dice[2]
        dice[2] = temp_dice[1]
    elif direc == 4:
        dice[5] = temp_dice[1]
        dice[6] = temp_dice[5]
        dice[2] = temp_dice[6]
        dice[1] = temp_dice[2]

for i in range(K):
    direc = directions[i]
    nx = x + dx[direc - 1]
    ny = y + dy[direc - 1]

    if 0 <= nx < N and 0 <= ny < M:
        # dice 굴리기
        roll(direc)
        # 지도 숫자 복사
        if maps[nx][ny] != 0:
            dice[6] = maps[nx][ny]
            maps[nx][ny] = 0
        else:
            maps[nx][ny] = dice[6]
        # dice 윗면 출력
        print(dice[1])
        x = nx
        y = ny
    else:
        continue