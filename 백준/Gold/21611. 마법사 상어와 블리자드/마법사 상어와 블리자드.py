dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

def get_score(M):
    score = 0
    for i in range(M):
        destroy(spells[i])
        score += explode()
        refill()
    return score


def destroy(spell):
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    d, s = spell
    sy, sx = shark
    for _ in range(s):
        sy += dy[d]
        sx += dx[d]
        matrix[sy][sx] = 0

    if is_empty():
        return
    
    marbles = get_marbles()
    arrange(marbles)


def explode() -> int:
    score = 0
    if is_empty():
        return score
    groups = get_groups()
    while need_explode(groups):
        marbles = []
        for group in groups:
            if len(group) < 4:
                marbles += group
        
            else:
                score += group[0] * len(group)

        arrange(marbles)
        
        if is_empty():
            return score
        groups = get_groups()

    return score


def need_explode(groups) -> bool:
    groups = get_groups()
    groups.sort(key = lambda x : len(x), reverse = True)
    return True if len(groups[0]) > 3 else False


def arrange(marbles):
    if len(marbles) < N ** 2 - 1:
        marbles += [0 for _ in range(N ** 2 - len(marbles) - 1)]

    d = 0
    step = 0
    index = 0
    ny, nx = shark
    while 0 <= ny < N and 0 <= nx < N:
        if d % 2 == 0:
            step += 1

        for _ in range(step):
            ny += dy[d]
            nx += dx[d]

            if ny < 0 or nx < 0:
                break

            matrix[ny][nx] = marbles[index]
            index += 1
        d = (d + 1) % 4


def refill():
    if is_empty():
        return
    groups = get_groups()
    marbles = []
    for group in groups:
        marbles.append(len(group))
        marbles.append(group[0])

    arrange(marbles)


def get_marbles():
    marbles = []
    d = 0
    step = 0
    ny, nx = shark
    while 0 <= ny < N and 0 <= nx < N:
        if d % 2 == 0:
            step += 1

        for _ in range(step):
            ny += dy[d]
            nx += dx[d]
            
            if ny < 0 or nx < 0:
                break

            marble_num = matrix[ny][nx]
            if marble_num != 0:
                marbles.append(marble_num)
        d = (d + 1) % 4

    return marbles + [0 for _ in range(N ** 2 - len(marbles) - 1)]


def get_groups():
    group = []
    groups = []
    marbles = get_marbles()
    marble_num = marbles[0]
    for i in range(len(marbles)):
        if marble_num != marbles[i]:
            groups.append(group)
            marble_num = marbles[i]
            group = []

        group.append(marbles[i])
    
    return groups


def is_empty():
    return sum(map(sum, matrix)) == 0


N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
spells = [None for _ in range(M)]
for i in range(M):
    d, s = list(map(int, input().split()))
    spells[i] = d - 1, s
shark = [N//2, N//2]
print(get_score(M))