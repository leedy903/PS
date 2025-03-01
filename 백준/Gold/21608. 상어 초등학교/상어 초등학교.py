N = int(input())
table = [list(map(int, input().split())) for _ in range(N*N)]
seats = [[None for _ in range(N)] for _ in range(N)]
seated = {}

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def count_emtpy_and_friends(friends: list, x: int, y: int):
    empty, friend = 0, 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < N and ny >= 0 and ny < N:
            if seats[ny][nx] is None:
                empty += 1
            if seats[ny][nx] in friends:
                friend += 1
    return empty, friend

for favorite in table:
    now = favorite[0]
    seated_favorite = []
    for i in range(1, 5):
        if favorite[i] in seated:
            seated_favorite.append(favorite[i])

    # 좋아하는 친구 중 하나라도 이미 앉았을 때
    if seated_favorite:
        max_count = []
        for i in range(N):
            for j in range(N):
                if seats[i][j] is None:
                    empty, friend = count_emtpy_and_friends(seated_favorite, j, i)
                    if not max_count:
                        max_count = [empty, friend, i, j]
                    if friend > max_count[1]:
                        max_count = [empty, friend, i, j]
                    elif friend == max_count[1] and empty > max_count[0]:
                        max_count = [empty, friend, i, j]
        
        seats[max_count[2]][max_count[3]] = now
        seated[now] = favorite[1:]

    # 좋아하는 친구가 아직 아무도 못앉았을 때
    else:
        max_count = []
        for i in range(N):
            for j in range(N):
                if seats[i][j] is None:
                    empty, friend = count_emtpy_and_friends([], j, i)
                    if not max_count:
                        max_count = [empty, i, j]
                    elif empty > max_count[0]:
                        max_count = [empty, i, j]
        
        seats[max_count[1]][max_count[2]] = now
        seated[now] = favorite[1:]

score = 0
for i in range(N):
    for j in range(N):
        favorite = seated[seats[i][j]]
        empty, friend = count_emtpy_and_friends(favorite, j, i)
        if friend == 0:
            score += 0
        elif friend == 1:
            score += 1
        elif friend == 2:
            score += 10
        elif friend == 3:
            score += 100
        elif friend == 4:
            score += 1000
print(score)