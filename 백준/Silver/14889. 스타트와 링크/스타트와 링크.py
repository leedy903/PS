N = int(input())
abilities = [list(map(int, input().split())) for _ in range(N)]
players = [False for _ in range(N)]

total_ability = sum(map(sum, abilities))
min_gap = total_ability


def dfs(depth, player):
    global min_gap, players
    if depth == N//2:
        start_ability, link_ability = 0, 0
        for y in range(N):
            for x in range(y + 1, N):
                if players[y] and players[x]:
                    start_ability += abilities[y][x] + abilities[x][y]

                if not players[y] and not players[x]:
                    link_ability += abilities[y][x] + abilities[x][y]

        min_gap = min(min_gap, abs(start_ability - link_ability))
        return


    for i in range(player, N):
        if not players[i]:
            players[i] = True
            dfs(depth + 1, i + 1)
            players[i] = False

dfs(0, 0)
print(min_gap)