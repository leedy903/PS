from collections import deque
def solution(maps):
    
    dy = [-1, 0, 1, 0]
    dx = [0, -1, 0, 1]
    
    n = len(maps)
    m = len(maps[0])

    def get_min_dist(start, end):
        dp = [[float('inf') for _ in range(m)] for _ in range(n)]
        deq = deque([start])
        dp[start[0]][start[1]] = 0
        while deq:
            y, x = deq.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < n and 0 <= nx < m:
                    if (maps[ny][nx] != 'X') and dp[ny][nx] > dp[y][x] + 1:
                        dp[ny][nx] = dp[y][x] + 1
                        deq.append([ny, nx])

        return dp[end[0]][end[1]]
    
    
    for y in range(n):
        for x in range(m):
            if maps[y][x] == 'S':
                start = [y, x]
            elif maps[y][x] == 'L':
                lever = [y, x]
            elif maps[y][x] == 'E':
                end = [y, x]
    answer = get_min_dist(start, lever) + get_min_dist(lever, end)
    if answer == float('inf'):
        answer = -1
    
    return answer