from collections import deque

def solution(board):
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
		
    n = len(board)
    INF = n * n * 600
    dp = [[[INF for _ in range(n)] for _ in range(n)] for _ in range(4)]
    
    route = deque()
    route.append([0, 0, 0, 0])
    route.append([0, 0, 0, 1])
    while route:
        y, x, cur_cost, cur_direction = route.popleft()
        for next_direction in range(4):
            ny = y + dy[next_direction]
            nx = x + dx[next_direction]
            if 0 <= ny < n and 0 <= nx < n and board[ny][nx] == 0:
                next_cost = cur_cost + 100
                if not cur_direction == next_direction:
                    next_cost += 500
                if next_cost < dp[next_direction][ny][nx]:
                    dp[next_direction][ny][nx] = next_cost
                    if ny == n - 1 and nx == n - 1:
                        continue
                    route.append([ny, nx, next_cost, next_direction])
    
    answer = INF
    for direction in range(4):
        answer = min(answer, dp[direction][n - 1][n - 1])
    return answer