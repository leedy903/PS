from collections import deque

def solution(maps):
    answer = 0
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]

    n = len(maps)
    m = len(maps[0])
    
    distance = [[-1 for _ in range(m)] for _ in range(n)]
    distance[0][0] = 1
    
    route = deque([])
    route.append([0, 0])
    
    while route:
        y, x = route.popleft()
        
        if (y == n - 1) and (x == m - 1):
            break
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < m and 0 <= ny < n:
                if maps[ny][nx] and distance[ny][nx] == -1:
                    distance[ny][nx] = distance[y][x] + 1
                    route.append([ny, nx])
    
    return distance[-1][-1]
